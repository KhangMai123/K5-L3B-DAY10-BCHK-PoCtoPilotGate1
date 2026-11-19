"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không tìm thấy chính sách hoàn tiền có hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def _ticket_order(ctx, action):
    order_id = ctx.ticket.get("order_id")
    if action.get("ticket_id") != ctx.ticket["ticket_id"] or action.get("order_id", order_id) != order_id:
        return None
    order = ctx.tools.lookup_order(order_id)
    if order is None or order["customer_id"] != ctx.ticket["customer_id"]:
        return None
    return order


def _tracking_parcel(ctx, order):
    if order is None or not order["parcels"]:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    parcel_id = ctx.ticket.get("parcel_id")
    if parcel_id and parcel["parcel_id"] != parcel_id:
        return None
    return parcel


def _refund_gate(ctx, action, order, parcel, policy):
    if parcel is None or policy is None or not parcel.get("delay_cause"):
        return Verdict.escalate("thiếu căn cứ tracking hoặc chính sách để hoàn tiền")
    delay = H.db_delay_days(parcel, ctx.as_of)
    entitlement = H.entitlement_vnd(policy, order, delay, parcel["delay_cause"])
    if entitlement <= 0:
        return Verdict.deny("tracking và chính sách hiệu lực không cho phép hoàn tiền")
    amount = action["amount_vnd"]
    if amount != entitlement or action.get("payer") != "LOGIX":
        return Verdict.escalate("số tiền hoặc bên chịu tiền khác căn cứ hoàn trong chính sách")

    rows = ctx.tools.ledger_rows(order_id=order["order_id"])
    if any(row["ticket_id"] == action["ticket_id"] for row in rows):
        return Verdict.deny("ticket đã có bút toán, bỏ qua lệnh ghi lặp")
    if rows:
        return Verdict.escalate("đơn đã có bút toán, cần kế toán đối soát trước khi hoàn thêm")

    approval_id = action.get("approval_id")
    if approval_id:
        approver = ctx.gates.get("operations", {}).get("approver_id")
        approvals = ctx.tools.lookup_approvals(approval_id=approval_id, ticket_id=action["ticket_id"],
                                               order_id=order["order_id"], customer_id=order["customer_id"])
        if not any(a["status"] == "valid" and a["expires_at"] >= ctx.as_of
                   and a["max_vnd"] >= amount and (not approver or a["approver_id"] == approver)
                   for a in approvals):
            return Verdict.escalate("phê duyệt không đúng ca, không hợp lệ hoặc không đủ hạn mức")
        return Verdict.allow()

    customer_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
    if amount > policy["auto_limit_vnd"]:
        return Verdict.escalate("khoản hoàn vượt hạn mức tự động của chính sách")
    if customer_cap is not None:
        customer_history = sum(row["amount_vnd"] for row in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                               if not row.get("approval_id"))
        # Lịch sử theo khách có cả bút toán cũ; tổng tự động trong ngày là cận trên thứ hai.
        customer_today_upper = min(customer_history, ctx.tools.auto_refund_today_vnd())
        if customer_today_upper + amount > customer_cap:
            return Verdict.escalate("chưa xác nhận còn đủ hạn mức hoàn tự động trong ngày cho khách")
    return Verdict.allow()


def _carrier_fault_gate(ctx, action, order, parcel, policy):
    if parcel is None or policy is None:
        return Verdict.deny("thiếu kiện hoặc chính sách để ghi lỗi hãng")
    delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("tracking không ghi nhận độ trễ và nguyên nhân đủ điều kiện ghi lỗi hãng")
    if not ctx.tools.ledger_rows(ticket_id=action["ticket_id"], order_id=order["order_id"]):
        return Verdict.deny("chưa có bút toán hoàn hợp lệ cho ticket")
    carrier_id = parcel["carrier_id"]
    if ctx.tools.lookup_carrier(carrier_id) is None:
        return Verdict.deny("không tìm thấy hãng chịu trách nhiệm trong danh mục đối tác")
    carrier_faults = ctx.tools.fault_rows(carrier_id=carrier_id)
    if any(f["order_id"] == order["order_id"] and f["parcel_id"] == parcel["parcel_id"] for f in carrier_faults):
        return Verdict.deny("kiện đã có bản ghi lỗi hãng")
    cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if cap is not None and len(carrier_faults) >= cap:
        return Verdict.deny("đã đủ số lỗi hãng tự động trong ngày; cần đối soát thủ công")

    fields = {"parcel_id": parcel["parcel_id"], "carrier_id": carrier_id,
              "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(key) != value for key, value in fields.items()):
        return Verdict.modify("lấy kiện, hãng, tài xế và độ trễ từ tracking", **fields)
    return Verdict.allow()


def _carrier_notice_gate(ctx, action, order, parcel, policy):
    if parcel is None or policy is None:
        return Verdict.deny("thiếu thông tin đối chiếu thông báo hãng")
    faults = ctx.tools.fault_rows(ticket_id=action["ticket_id"], order_id=order["order_id"],
                                  parcel_id=parcel["parcel_id"], carrier_id=action.get("carrier_id"))
    if not faults or action.get("carrier_id") != parcel["carrier_id"]:
        return Verdict.deny("thông báo không có lỗi hãng tương ứng trong sổ ghi lỗi")

    source = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
              "district": order["recipient"].get("district"), "delay_days": faults[0]["delay_days"]}
    legal = ctx.gates.get("legal", {})
    blocked = set(legal.get("pii_fields_blocked_to_third_party") or [])
    allowed = set(policy["carrier_notice_fields"]) - blocked
    payload = {key: value for key, value in source.items() if key in allowed and value is not None}
    if not payload:
        return Verdict.deny("không còn trường được phép gửi cho hãng")
    if payload != action.get("payload"):
        return Verdict.modify("tạo thông báo từ các trường nghiệp vụ được phép", payload=payload)
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    order = _ticket_order(ctx, action)
    parcel = _tracking_parcel(ctx, order)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if tool == "issue_refund":
        return _refund_gate(ctx, action, order, parcel, policy)
    if tool == "file_carrier_fault":
        return _carrier_fault_gate(ctx, action, order, parcel, policy)
    return _carrier_notice_gate(ctx, action, order, parcel, policy)
