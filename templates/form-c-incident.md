# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** BCHK · **Thẻ đã bốc:** S6 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S6-prepared-20261119-165522-84d2be` | S6 · prepared | Đo từ bản chốt trước khi sửa vòng 2 | 0,8333 [0,5833; 1,0000] | 0,8333 | 270.000 · 10 · 0 | 0% | Cổng vòng 1 sửa nhầm kiện và giữ trần lỗi; hai ticket thiếu mã kiện vẫn gây tác hại. |
| 2 | `R-S6-after-20261119-165745-9bffb7` | S6 · after | Chuyển duyệt trước khi ghi nếu thiếu mã kiện và nhiều kiện đủ ngưỡng trễ | 1,0000 [1,0000; 1,0000] | 1,0000 | 0 · 0 · 0 | 16,67% | 10 lượt chuyển duyệt trước ghi. Chi phí 5.228 đồng/ticket và 0 ca ùn. |
| 3 | `R-S6-after-20261119-165819-bc3e46` | S6 · after | Thêm chỉ số đối chiếu lỗi theo kiện và tỷ lệ chuyển duyệt do thiếu mã kiện | 1,0000 [1,0000; 1,0000] | 1,0000 | 0 · 0 · 0 | 16,67% | Hai chỉ số theo dõi không làm đổi quyết định nghiệp vụ; tỷ lệ lệch tracking về 0. |
| 4 | `R-base-after-20261119-165819-bc3e46` | base · after | Kiểm hồi quy bộ nền sau cổng xác minh kiện S6 | 1,0000 [1,0000; 1,0000] | 1,0000 | 0 · 0 · 0 | 22,73% | 110/110 lượt đạt, không có ca mới hỏng. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S6
```

- Mã lần chạy grade `R-S6-grade-20261119-165522-84d2be` · base `R-S6-before-20261119-165522-84d2be` · prepared `R-S6-prepared-20261119-165522-84d2be`.
- Vòng 1 giảm lỗi hãng oan từ 40 xuống 10 và nâng pass_rate từ 0,3333 lên 0,8333 (20/60 → 50/60). G2 dùng đúng kiện ở `S6-01`–`S6-04` và chặn lỗi thứ ba, thứ tư ở `S6-42`–`S6-43`. Hai ticket `S6-20` và `S6-21` vẫn được hoàn khi chưa xác định kiện. Tổng hoàn sai giữ ở 270.000 đồng trên 10 lượt thử, ngày giả lập tệ nhất 54.000 đồng. Lộ PII giữ 0.
- `prepared` có 0 ca ùn, chờ lâu nhất 0 phút, chi phí 3.595 đồng/ticket, ROI 0,53, tiền máy cao nhất 767/1.500 đồng và hoàn tự động tối đa 96.000/1.600.000 đồng/ngày. `ops.violations` rỗng. Hai sàn chất lượng 0,97 và 0,91 cùng hai trần an toàn về tiền hoàn sai và lỗi hãng oan vẫn trượt. HCM có 10 lỗi oan và pass_rate 0,5; phân khúc DNB có 5 lỗi oan và pass_rate 0,5.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Lăng kính kỹ thuật (đơn vị gán lỗi), pháp lý (trách nhiệm đối tác) và vận hành (xác minh kiện và duyệt vượt trần). Hậu quả kinh doanh gồm phí hoàn sai và công đối soát.
- Phiếu B mục B6 đã dự báo ghi lỗi của kiện khác. Bản chốt giảm 30/40 lỗi oan, nhưng B6 chưa đặt quy tắc khi thiếu mã kiện và nhiều kiện đều đủ ngưỡng. Xác định đúng hãng của một kiện không đủ để biết khách đang hỏi về kiện nào.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Trợ lý đã tự chọn kiện dù nhiều kiện đều đủ ngưỡng, rồi ghi cả tiền và lỗi hãng. | Kỹ thuật và vận hành | `S6-20@11`, `S6-21@11` ở prepared; đối chiếu `ticket.parcel_id` và `tracking.parcels`. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite S6 --stage base --ticket S6-01 --seed 11
python3 -m lab10.trace --suite S6 --stage prepared --ticket S6-20 --seed 11
python3 -m lab10.trace --suite S6 --stage base --ticket S6-43 --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ.** Hãng và tài xế có thể bị phạt hoặc trừ thưởng vì ghi lỗi oan. Base có 40 lỗi hãng oan trên 60 lượt và 270.000 đồng hoàn sai. Bộ thử đo bản ghi và tiền hoàn, chưa đo số tiền thưởng bị trừ.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11`, base. Dòng 02 có P1/GHSH trễ 0 ngày, P2/VNX trễ 4 ngày; ticket chỉ định P2. Dòng 06 ghi P1/GHSH, tài xế `TX-GHSH-06`, trễ 4 ngày. Dòng 07 báo GHSH. | Điều phối GHSH, tài xế P1 và kế toán. | Cao | Lỗi chìm. Khách nhận đúng 30.000 đồng nhưng bên giao đúng hạn bị gán lỗi. |
| 2 | `S6-20@11`, prepared. Dòng 02 có hai kiện trễ 3 và 5 ngày, thiếu mã kiện. Dòng 04 dùng 5 ngày, dòng 05 ghi 26.000 đồng, dòng 07 ghi lỗi VNX. `S6-21@11` có hai kiện cùng trễ 4 ngày, được ghi hoàn 28.000 đồng và lỗi DNB theo thứ tự danh sách. | VNX, DNB, khách và người đối soát. | Cao | Lỗi ngữ cảnh. Mô tả cấp đơn bị dùng cho quyết định cấp kiện. |
| 3 | `S6-43@11`, base. Dòng 06 ghi lỗi GHSH thứ tư trong chuỗi `S6-LOAT`, dòng 07 gửi hãng dù trần là 2 lỗi tự động mỗi hãng mỗi ngày. | GHSH, tài xế và Oanh. | Cao | Lỗi chìm. Khoản hoàn 24.000 đồng hợp lệ, nhưng lỗi thứ tư cần đối soát tay. |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Có mã kiện P2. Lệnh ghi dùng P1. | Thiếu mã kiện; agent lấy độ trễ cực đại hoặc thứ tự khi đồng hạng. | Ticket riêng lẻ có thể hợp lệ. Các ca dùng chung một sổ lỗi. |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | Tracking đủ, tham số lệnh ghi lệch nguồn chuẩn. | Tracking có nhiều kiện đủ ngưỡng, chưa xác định kiện khách đang hỏi. | Sổ lỗi và `ops_limits` có dữ liệu hạn mức, base chưa kiểm. |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Mã đơn nhóm nhiều kiện; tracking theo kiện xác định hãng, tài xế, độ trễ. | Mã kiện đã xác minh hoặc xác nhận của CSKH có giá trị hơn phép chọn kiện chậm nhất. | Sổ lỗi theo hãng/ngày quyết định còn được ghi tự động. |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Tính tiền theo kiện chậm nhất và ghi lỗi theo kiện đầu khiến quyết định lệch nhau. | Thiếu định danh và quy tắc mặc định gây cả hoàn sai và lỗi oan. | Lặp thao tác đủ nhiều trong ngày vượt trần, dù mỗi ca có lý do riêng. |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng giao đúng hạn nhận thông báo trễ của kiện khác. | Hãng bị xác định theo số ngày hoặc vị trí dù khách chưa xác minh kiện. | Lỗi tự động vượt giới hạn đã thống nhất với đối tác. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Đối chiếu tham số với tracking, sửa trước ghi hoặc chặn khi thiếu căn cứ. | Chuyển Hạnh trước khi ghi tiền để xác minh. | Giữ khoản hoàn hợp lệ và chuyển phần kiểm lỗi vượt trần sang đối soát. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Oanh kiểm mã kiện và tài xế, lập đính chính nếu đã ghi sai. | Hạnh hỏi mã kiện hoặc tra chứng từ, sau đó quyết định quyền lợi và trách nhiệm. | Oanh tìm sự kiện `carrier_fault_review_required`; Hạnh xác nhận nếu cần xử lý thủ công. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `carrier_parcel_mismatch_rate` cho biết độ lệch bản ghi và tracking. | `ambiguous_parcel_handoff_rate` cho biết số lượt cần xác định kiện. | Dùng sự kiện giữ lỗi vượt trần và `wrongful_carrier_faults` để theo dõi. |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

|  | Nhóm A · Điều phối hãng và tài xế | Nhóm B · Kế toán đối soát |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Điều phối nhận thông báo ghi lỗi và kiểm lịch giao của tài xế. | Oanh đọc sổ lỗi, thông báo và sổ hoàn khi đối soát với hãng, shop. |
| Mục tiêu chính của họ | Quy trách nhiệm đúng kiện, đúng chặng và người bàn giao. | Đối soát tiền hoàn và khoản phạt với căn cứ và chủ thể đúng. |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | Tra mã kiện, so ngày hẹn với lượt quét giao, rồi tìm hãng và tài xế giữ kiện tại chặng trễ. | Nối mã đơn + mã kiện với sổ lỗi. So nguyên nhân theo chính sách, trần ngày rồi xác minh chứng từ trước khi tính phạt. |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Feed và mã vận đơn giữa các hãng có thể khác; ca thiếu quét cần tra thủ công. | Quy tắc đối soát nhất quán, mức độ sẵn có chứng từ theo hãng có thể khác. |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | Kiện và chặng cụ thể, gắn tài xế theo thời điểm. | Khoản hoàn có thể ghi cấp đơn, trách nhiệm hãng được xét theo kiện/chặng và sổ lỗi theo ngày. |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Bản base gán hãng đại diện cấp đơn. `S6-01@11` dòng 02 ghi P2/VNX trễ 4 và P1/GHSH trễ 0, còn dòng 06 ghi lỗi P1/GHSH với độ trễ của P2.
- Điều phối và kế toán dùng kiện và chặng. Agent lấy kiện trễ nhất để tính tiền rồi lấy kiện đầu để gán hãng và tài xế.
- Prepared sửa tham số lỗi theo tracking nhưng vẫn đoán kiện chậm nhất (`S6-20@11`) hoặc lấy kiện đầu khi đồng hạng (`S6-21@11`). Cần chuyển xác minh trước khi ghi tiền, ghi lỗi hoặc gửi hãng.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id`, `carrier_id`, `driver_id`, `delay_days` | WRONG | Dòng 06 của `S6-01@11` base gán độ trễ 4 ngày của P2/VNX cho P1/GHSH giao đúng hẹn. | Hãng và tài xế P1 có thể bị phạt oan; Oanh phải điều chỉnh sổ. | Vòng 1 G2 căn lại tham số theo tracking; dòng 06–07 ở prepared xác nhận. | Giữ G2 trước ghi và đo sai lệch giữa bản ghi và tracking. Tầng chặn và phát hiện. |
| `ticket.parcel_id` và tập kiện đủ ngưỡng | INCOMPLETE | `S6-20@11` có hai kiện trễ 3 và 5 ngày, thiếu mã kiện; prepared tự chọn P2. `S6-21@11` đồng hạng 4 ngày. | Hoàn khi chưa xác định quyền lợi, phạt hãng thiếu căn cứ. | G2 kiểm hãng của kiện đã chọn; bản chốt chưa kiểm mơ hồ trước ghi tiền. | Chuyển Hạnh trước `issue_refund` nếu thiếu mã và nhiều kiện đủ ngưỡng. Tầng chặn. |
| Số lỗi tự động theo hãng/ngày | PERTURBED | `S6-40`–`S6-43` chạy cùng ngày giả lập; base ghi lỗi thứ tư ở `S6-43@11` dù trần là 2. | Lỗi cộng dồn ảnh hưởng thưởng/phạt của hãng nhỏ. | Vòng 1 đã giữ tối đa hai lỗi và vẫn ghi khoản hoàn hợp lệ. | Giữ trần trong `_carrier_fault_gate`, ghi dấu ca cần Oanh đối soát. Tầng giới hạn và vận hành. |
| `driver_id` trong nguồn tracking | INVALID | Kịch bản chưa thấy trên trace: tracking vẫn dùng tài xế cũ sau khi bàn giao chặng. | Bản ghi có thể đúng kiện và hãng nhưng ảnh hưởng nhầm tài xế. | G2 lấy tài xế từ tracking. Dữ liệu cung cấp sai từ nguồn có thể lọt qua. | Đối chiếu nhật ký phân công theo chặng và thời điểm trước khi áp chế tài. Tầng phát hiện và vận hành. |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc report. Mỗi bản ghi lỗi tự động phải khớp kiện thuộc đơn của ticket và hãng, tài xế, độ trễ theo tracking, có nguyên nhân được policy đúng ngày chấp nhận và còn hạn mức của hãng. Khi ticket đi tới bước ghi hoàn mà thiếu mã kiện và có ít nhất hai kiện đạt ngưỡng trễ, phải đưa cho người duyệt trước khi ghi tiền, ghi lỗi hoặc gửi hãng.

Kiểm bằng `write_gate` trước `issue_refund`, `_carrier_fault_gate` trước ghi lỗi và `_carrier_notice_gate` trước gửi hãng. So `ledger`, `fault_rows` và outbound ở trace S6; kết quả tổng hợp nằm ở `wrongful_refund_vnd`, `wrongful_carrier_faults` và `carrier_parcel_mismatch_rate`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định môi trường. Kênh CSKH có thể thu được mã kiện đủ sớm và nguồn tracking nối được mã đó với hãng/tài xế đang phụ trách kiện tại thời điểm giao.

Khách qua app, Zalo hoặc điện thoại có thể chỉ biết mã đơn. Dữ liệu quét và phân công giao có thể đến muộn sau khi đổi tài xế hoặc hãng ở một chặng.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-before-20261119-165522-84d2be`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Hãng/tài xế nhận lỗi oan, có thể bị trừ thưởng (40 lỗi ở base)
 └─ HOẶC
    ├─ [1] Tool ghi lỗi cho kiện đại diện sai (tầng hành động)
    │  └─ S6-01@11 base: tracking P2/VNX trễ 4, tool lại ghi P1/GHSH trễ 4.
    ├─ [2] Đoán kiện khi chưa biết khách đang hỏi kiện nào (tầng dữ liệu/quyết định)
    │  └─ S6-20@11 và S6-21@11 prepared: thiếu mã kiện, nhiều ứng viên, vẫn ghi hoàn và lỗi.
    └─ [3] Ghi dồn lỗi tự động vượt trần cùng hãng (tầng vận hành/quyền ghi)
       └─ S6-43@11 base: lỗi thứ tư của GHSH cùng ngày trong S6-LOAT, trần cho phép 2.
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Lỗi và thông báo phải trỏ đúng kiện, hãng, tài xế và độ trễ từ tracking. | Đơn có thể tách nhiều kiện và hãng. Kiện đầu không đại diện cả đơn. |
| [2] | Thiếu mã và có nhiều kiện đạt ngưỡng thì người duyệt xác minh trước mọi ghi hoàn/lỗi/gửi hãng. | Khách có thể chỉ nêu mã đơn; kiện chậm nhất chưa chắc là kiện họ đang hỏi. |
| [3] | So số lỗi tự động theo hãng/ngày trước ghi; khoản hoàn hợp lệ không tạo quyền vượt giới hạn ghi lỗi. | Ca cùng hãng có thể tới dồn dập. Điều phối và kế toán cần kiểm riêng lỗi vượt trần. |


---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite S6 --stage after --note "Thêm chỉ số đối chiếu lỗi theo kiện và tỷ lệ chuyển duyệt do thiếu mã kiện"
python3 -m lab10.grade --incident S6
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Bản ghi gán kiện đầu dù tính theo kiện khác. | Giữ `_tracking_parcel`, `_carrier_fault_gate` và `_carrier_notice_gate` của vòng 1. `carrier_parcel_mismatch_rate` đối chiếu các bản ghi đã tạo. | Chặn và phát hiện | Ngăn ghi sang kiện/hãng khác khi tracking đúng; chỉ số báo nếu sổ lỗi đã lệch. | `R-S6-after-20261119-165820-bc3e46` |
| [2] | Ticket thiếu mã kiện, nhiều kiện trễ đủ ngưỡng. | Thêm nhánh `write_gate` trước `issue_refund`. Đếm số kiện đạt `policy.late.min_days_fee` từ tracking. Nếu thiếu mã kiện và số kiện trên 1, ghi `ambiguous_parcel` và chuyển duyệt. | Chặn trước ghi | Ngăn gán sai tự động ở luồng ghi đã kiểm. Hạnh xác minh để phục vụ tiếp; không suy ra mã kiện từ vị trí hoặc độ trễ lớn nhất. | `R-S6-after-20261119-165745-9bffb7` · `R-S6-after-20261119-165820-bc3e46` |
| [3] | Các lỗi cùng hãng phát sinh dồn trong ngày. | Giữ `_carrier_fault_gate` với `max_auto_strikes_per_carrier_per_day=2`. Ghi thêm `carrier_fault_review_required` để Oanh đối soát các lần bị giữ. | Giới hạn thiệt hại và vận hành | Ngăn ghi lỗi tự động từ lần thứ ba trong ngày giả lập. Hoàn hợp lệ vẫn chạy. Sự kiện là đầu mối chuyển đối soát, việc bàn giao còn cần runbook. | `R-S6-after-20261119-165820-bc3e46` |

Đối chứng bằng trace `S6-20@11` và `S6-21@11` mốc after. Cổng chuyển duyệt trước khi ghi; sổ cái, sổ lỗi và thông báo hãng đều rỗng. `S6-43@11` vẫn hoàn 24.000 đồng, có sự kiện giữ lỗi theo trần và không tạo lỗi hay thông báo mới. Kiểm bổ sung trong bộ nhớ cho thấy đơn chỉ có một kiện đủ ngưỡng vẫn được phục vụ khi thiếu mã, hai lựa chọn mã kiện hợp lệ dẫn tới đúng hãng/tài xế, mã ngoài đơn được chuyển duyệt và câu hỏi trạng thái vẫn được trả lời. Bộ kiểm thử công khai đạt 13/13.

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `carrier_parcel_mismatch_rate`. |
| **Bước / hành vi được đo** | Đối chiếu phát sinh thực tế ở `file_carrier_fault` với kiện của ticket và tracking lúc xử lý. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ lượt có ít nhất một bản ghi lỗi lệch đối chiếu, đơn vị là tỷ lệ từ 0 đến 1 (hoặc %). |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `ticket.parcel_id` nếu có, `events.tracking.parcels` và `faults` trong trial. So mã kiện, mã hãng và số ngày trễ. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Tử số đếm mỗi lượt một lần nếu có lỗi ghi cho kiện khác mã đã nêu, hoặc bộ ba kiện/hãng/độ trễ không khớp tracking. Có lỗi ghi nhưng thiếu tracking được tính vào tử số. Mẫu số là tổng lượt; danh sách rỗng trả 0 trong lab, trên bảng trực vận hành hiển thị thêm cỡ mẫu. |
| **Khung thời gian / ngưỡng báo động** | Dùng cửa sổ 60 phút, rà lại khi ghi lỗi. Từ một lượt lệch, Tùng tạm dừng `file_carrier_fault` và `notify_carrier` ở luồng liên quan, Oanh đối chiếu trước khi mở lại. |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Chỉ số có thể bằng 0 nếu tracking chứa sai tài xế/nguồn quét hoặc một kiện được tự chọn tình cờ khớp bản ghi. Chỉ số riêng về chuyển duyệt xử lý trường hợp thiếu định danh đã phát hiện. |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Báo cáo `R-S6-grade-20261119-165820-bc3e46`. Base chưa có cổng: bộ nền 1/110 = 0,009091, S6 25/60 = 0,416667. Mốc after: cả hai bộ bằng 0. |

**Chỉ số chuyển xác minh.** `ambiguous_parcel_handoff_rate` lấy số lượt có ít nhất một sự kiện `guard` với `kind=ambiguous_parcel` chia tổng lượt. After trên bộ nền 0/110; trên S6 10/60 = 0,166667 theo `R-S6-grade-20261119-165820-bc3e46`. Sự kiện cho biết cổng đã bắt được ca cần xác minh, chưa chứng minh người duyệt đã xử lý đúng. Hạnh theo dõi trong 60 phút, rà nguồn thiếu mã khi tỷ lệ vượt 25% và gọi dự phòng theo hàng chờ ở B7.5–B7.6.

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-after-20261119-165820-bc3e46`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hãng/tài xế nhận lỗi oan và có thể chịu chế tài
 └─ HOẶC
    ├─ [1] Tham số lấy từ kiện đại diện VÀ [cổng đối chiếu tracking hỏng]
    ├─ [2] Ticket thiếu mã, nhiều kiện trễ VÀ [cổng chuyển xác minh không giữ lệnh ghi]
    └─ [3] Lỗi cùng hãng dồn vượt trần VÀ [cổng kiểm số lỗi ngày hỏng]
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `_carrier_fault_gate`, `_carrier_notice_gate` và `carrier_parcel_mismatch_rate`. | Chặn và phát hiện | Ngăn ghi/gửi sang hãng khác khi dữ liệu kiện đúng; theo dõi cả lỗi đã thoát qua gate. | Tracking có thể ghi sai hoặc cũ về chặng/tài xế. Cần đối chiếu với log phân công. |
| [2] | `write_gate` trước `issue_refund` và `ambiguous_parcel_handoff_rate`. | Chặn trước ghi và phát hiện | Khi có nhiều kiện đủ ngưỡng và chưa có mã kiện, luồng tự động chuyển duyệt với 0 ghi tiền, 0 lỗi, 0 gửi. | Người duyệt có thể thiếu chứng từ hoặc khách cung cấp mã hợp lệ của kiện khác. Trợ lý có thể từ chối sớm trước khi tới điểm ghi; CSKH cần đường xác minh. |
| [3] | `_carrier_fault_gate` và sự kiện `carrier_fault_review_required`. | Giới hạn và vận hành | Ngăn lỗi tự động vượt trần trong một sổ lỗi ngày giả lập; giữ hoàn tiền hợp lệ. | Production cần sổ lỗi dùng chung giữa worker, phân ngày nhất quán, kiểm trần cùng giao dịch và xác nhận ca thủ công. |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tracking trễ hoặc sai hãng/tài xế do bàn giao chặng chưa cập nhật. | Có thể xảy ra khi đồng bộ nhiều hãng; chưa đo. | Cao. Gán lỗi sai có thể dẫn tới thưởng/phạt sai dù logic đối chiếu chạy đúng. | Phạm Kiều Oanh | `carrier_parcel_mismatch_rate` từ một lượt lệch trong 60 phút; kiểm mẫu độc lập với tracking để phát hiện lỗi cùng nguồn. | Tùng giữ ghi lỗi/gửi hãng liên quan, Oanh đối chiếu mã kiện và chứng từ phân công theo thời điểm. | Hoãn bật lại ghi lỗi ở luồng liên quan tới khi đã sửa dữ liệu và đối soát. | MAP · MEASURE |
| Nhiều yêu cầu cấp đơn thiếu mã kiện, dồn ca về người duyệt. | Trung bình ở kênh chưa thu mã; 10/60 lượt S6 after đã chuyển theo lý do này. | Cao nếu dồn ca. Khách chờ, phát sinh công duyệt; nhân viên có thể chọn kiện khi thiếu căn cứ. | Trần Thị Hạnh | `ambiguous_parcel_handoff_rate` trên 25% trong 60 phút, hoặc `queue_wait_max_min` từ 30 phút. | Xác minh kênh thiếu mã, bố trí dự phòng, giữ giao dịch chưa xác minh; tạm dừng nhận mới nếu vượt SLA hoặc có ca ùn. | Hoãn mở thêm kênh nếu chưa đủ dữ liệu và người duyệt. | MANAGE |
| Ca không tra được đơn/kho đi qua model rồi vẫn chuyển tay. | Có trong bộ nền, chưa biết tỷ lệ thực tế. | Chi phí nhóm `?` vượt làm tay; có thể mở sai phạm vi pilot nếu chỉ nhìn chi phí toàn bộ. | Nguyễn Tấn Châu | `ops.segments[?].cost_per_ticket_vnd` vượt 10.000 đồng/ticket; after đo 10.359 đồng. | Thử xác minh mã đơn và kho trước model, chuyển thẳng ca thiếu dữ liệu sang CSKH; đo cả đường xử lý và phần còn lại. | Giữ Cải tiến thêm cho tới khi chứng minh phần giữ lại đáp ứng các ngưỡng. | MEASURE · MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 · Chất lượng | Xong | `R-S6-grade-20261119-165820-bc3e46` và `R-base-after-20261119-165819-bc3e46` xác nhận 60/60 S6, 110/110 bộ nền, không hồi quy. Kiểm ẩn do bộ chấm thực hiện. | Nguyễn Văn Hậu |
| 2 · Dữ liệu | Chưa | C3.2–C5 xác định khóa theo kiện; cần xác minh với các hãng độ trễ đồng bộ mã chặng, hãng và tài xế trước pilot. | Nguyễn Tấn Châu |
| 3 · Bảo mật | Xong | C7 và report after thấy PII = 0, thông báo lấy các trường trong danh sách được phép; đã đối chiếu bước gửi đúng hãng trong mô phỏng. | Mai Xuân Khang |
| 4 · Quyền hạn | Xong | C7–C9. Hai lỗi đầu của cùng hãng trong chuỗi `S6-LOAT` được phép; các ca vượt trần đã giữ. Hai ticket chưa rõ kiện không ghi bút toán. | Lê Thanh Tùng |
| 5 · Hiệu năng, hạ tầng | Chưa | S6 after `R-S6-after-20261119-165820-bc3e46` chờ tối đa 0 phút nhưng chưa kiểm tải cụm theo phút và giới hạn dùng chung giữa các worker. | Mai Xuân Khang |
| 6 · Chi phí | Chưa | Mốc S6 `R-S6-after-20261119-165820-bc3e46` đạt 5.228 đồng/ticket và ROI 0,91; bộ nền `R-base-after-20261119-165819-bc3e46` có nhóm `?` 10.359 đồng/ticket. Cần đo định tuyến tay trực tiếp. | Phạm Kiều Oanh |
| 7 · Vận hành | Chưa | Runbook 4–5 quy định trực 1 người, 6 ca/giờ, SLA 60 phút và mốc dự phòng. Chưa diễn tập nhận cảnh báo, dừng thao tác và xử lý tồn với lịch trực thật. | Trần Thị Hạnh |
| 8 · Con người, pháp lý | Chưa | C3.2 và C8 có cách đối chiếu theo kiện/hãng, giới hạn gửi dữ liệu và số đo 0 PII. Cần kiểm luồng đính chính với đối tác và bằng chứng nguồn theo chặng. | Lê Quân Bảo |
| 9 · Quyết định | Xong | Phiếu A và B8 giữ nguyên. C12 ghi v2 Cải tiến thêm, kèm báo cáo `R-S6-grade-20261119-165820-bc3e46` và điều kiện đo lại. | Mai Xuân Khang |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Số lỗi oan và đối chiếu thông báo ở B7.5 đáng lẽ báo trước khi đối soát tiền phạt. Bản base có log tracking và sổ lỗi nhưng thiếu phép đối chiếu cấp kiện. Vòng 2 thêm `carrier_parcel_mismatch_rate` và tỷ lệ chuyển duyệt do thiếu mã. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Từ chưa có ngưỡng tự động theo tín hiệu lệch sang cảnh báo đỏ khi có từ 1 lượt lệch trong 60 phút. Với tỷ lệ chuyển xác minh, trên 25% trong 60 phút thì rà kênh thiếu mã và tải duyệt. Trần 2 lỗi tự động mỗi hãng/ngày, SLA 60 phút và thời hạn dừng 10 phút giữ theo vòng 1. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 người trực, 6 ca/giờ; Hạnh đứng tên duyệt, Tùng giữ công tắc. Oanh nhận sự kiện giữ lỗi vì trần để đối soát. Hạnh gọi một người dự phòng có quyền khi có từ 3 ca chờ hoặc chờ lâu nhất từ 30 phút. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ 100% phạm vi bộ thử và kiểm mẫu 10% quyết định tự động kèm ghi chú. Trước lệnh ghi, người duyệt xác minh ca thiếu mã mà có nhiều kiện đủ ngưỡng. Chỉ đối soát tay phần lỗi vượt trần khi bút toán hoàn đã hợp lệ. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Oanh báo cho đầu mối hãng liên quan trong 1 giờ từ khi xác nhận lỗi, cung cấp mã kiện, ngày, phạm vi ảnh hưởng và trạng thái đối soát. Hãng chuyển thông tin cần thiết cho tài xế. Hạnh thông báo khách về trạng thái hoàn nếu giao dịch bị ảnh hưởng. Tùng dừng thao tác liên quan trong tối đa 10 phút; Oanh đính chính sổ lỗi và đề nghị rà lại thưởng/phạt sau xác minh. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Report S6 ghi 0 lần lộ theo phép đo. Nếu đối soát phát hiện thông tin cá nhân bị gửi ngoài, Tùng dừng `notify_carrier`; Oanh báo đầu mối quyền riêng tư và hãng, khoanh trường và người nhận trước khi lên phương án thông báo. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Thẻ mô tả phản ánh của người trong hãng về thưởng bị trừ. Trace sau đó xác định nhầm kiện và ghi vượt trần. Lab thiếu nhật ký phân công chặng và dữ liệu thưởng/phạt thực tế để định lượng tác động ngoài sổ lỗi. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu ticket tăng gấp 3 lần trong một giờ, Hạnh kiểm lượng chờ. Có từ 3 ca chờ hoặc chờ lâu nhất từ 30 phút thì gọi 1 người dự phòng có quyền. Tùng chuyển bớt nhận mới sang CSKH nếu chờ tới 45 phút và tiếp tục tăng. Dừng nhận mới khi chờ quá 60 phút hoặc có 1 ca ùn.
2. Nếu lỗi LLM kéo quá 5 phút, Hạnh đặt chế độ xử lý tay cho luồng bị ảnh hưởng; Tùng kiểm nguồn lỗi và tạm giữ thao tác ghi tự động cần thiết. Mở lại sau ca thử khớp sổ cái, tracking và xác nhận ca chờ trong SLA.
3. Nếu người duyệt nghi một quyết định, Hạnh giữ lệnh đang chờ và đối chiếu mã kiện, mốc giao, người phụ trách, policy và phê duyệt. Khi xác nhận lỗi hãng oan, Tùng tắt luồng ghi lỗi và gửi hãng trong tối đa 10 phút, Oanh rà các bản ghi liên quan trước bật lại.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `c3d3b19bbc35c449dc203685ce985c5bcce7f5ed`. |
| Hash chốt cổng vòng 1 | `1cccd450` (`1cccd4501a46e40a18957c5af907aaae9718727697fd3e247db731d3ca1e26fe`). |
| Mã lần chạy dùng làm bằng chứng | S6 · base `R-S6-before-20261119-165820-bc3e46` · prepared `R-S6-prepared-20261119-165820-bc3e46` · after `R-S6-after-20261119-165820-bc3e46`. |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Report tổng không có vi phạm vận hành/kinh doanh, và mọi ngưỡng đã ký đều đạt. S6 after chờ 0 phút, 0 ca ùn, hoàn tự động tối đa 96.000/1.600.000 đồng/ngày, tiền máy cao nhất 767/1.500 đồng và lộ PII bằng 0. Bộ nền vẫn có chi phí nhóm `?` cao hơn làm tay. |
| Kho hoặc hãng có số xấu nhất. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | HCM có chi phí cao nhất trong S6 after, 5.661 đồng/ticket (20 lượt), thấp hơn làm tay. Mọi kho và hãng trong S6 đạt 100%, hoàn sai, lỗi oan và PII bằng 0. Nhóm chưa gắn kho `?` của bộ nền là 10.359 đồng/ticket, cao hơn làm tay 359 đồng. Chỉ nhìn HCM thì có thể cân nhắc tiếp tục phạm vi HCM đã mô phỏng; nhìn nhóm `?` vẫn cần cải tiến. |
| Quyết định (khoanh một) | **Cải tiến thêm** |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | S6 `R-S6-after-20261119-165820-bc3e46` đạt 60/60 (pass_rate và pass⁵ đều 1,0000), gồm 20/20 lượt hợp lệ và độ phủ 100%. Hai sàn ký là 0,97 và 0,91. Bộ nền `R-base-after-20261119-165819-bc3e46` đạt 110/110, 0 ca mới hỏng. |
| Bằng chứng 2 | S6 `R-S6-before-20261119-165820-bc3e46` → `R-S6-prepared-20261119-165820-bc3e46` → `R-S6-after-20261119-165820-bc3e46`. Lỗi hãng oan 40 → 10 → 0, tiền hoàn sai 270.000 → 270.000 → 0 đồng, PII giữ 0. Tỷ lệ chuyển duyệt after 16,67% (10/60), dưới ngưỡng ký 25%. |
| Bằng chứng 3 | S6 `R-S6-after-20261119-165820-bc3e46` có chi phí 5.228 đồng/ticket, ROI 0,91 và 0 ca ùn. Bộ nền `R-base-after-20261119-165819-bc3e46` đạt chi phí chung 4.456 đồng/ticket và ROI 1,24 nhưng nhóm `?` vẫn qua người duyệt ở 5/5 lượt với chi phí 10.359 đồng/ticket. |
| Khớp dòng nào trong `decision_rule` đã ký? | `decision_rule.Cải tiến thêm`. Chi phí của luồng chưa rõ kho còn vượt xử lý tay. Chưa có phép đo chứng minh loại ca này được định tuyến thẳng và phần giữ lại đạt các trần khi chạy tại hai depot. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không áp dụng ở v2. Giữ độ phủ mô phỏng 100%. Khách thật tiếp tục dùng xử lý tay trong lúc kiểm lại tuyến vào. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Mở rộng bước xác minh ở đầu vào ngay trước khi gọi mô hình: mã đơn/kho để định tuyến tay khi thiếu, mã kiện để chuyển người trước khi áp lỗi theo nhánh [2]. Châu và Khang đo chi phí luồng chưa rõ kho ≤ 10.000 đồng/ticket. Hạnh và Oanh diễn tập xác minh kiện/người giao và SLA. Đối chiếu lại chỉ số an toàn và các ngưỡng đã ký trên phần giữ lại. Hạn 20/11/2026. |
| Nếu Dừng: bài học ghi lại | Không áp dụng. S6 đã đạt ba ngưỡng an toàn trong bộ thử nhìn thấy và có hướng giải quyết phần định tuyến còn tốn chi phí. |
| Ngày quyết định lại (trừ khi Dừng) | 20/11/2026 (UTC+7), sau khi có kết quả đo tuyến vào và diễn tập đối soát ở phạm vi dự định. |
| PIC ký | Mai Xuân Khang (2A202603722), trưởng nhóm phụ trách Gate 1. |

**Chỉ ở v2**
- Giữ Cải tiến thêm. S6 đã giảm hoàn sai về 0 và lỗi hãng oan về 0, nhưng luồng `?` của bộ nền vẫn 10.359 đồng/ticket, cao hơn xử lý tay như ở v1.
- Báo cáo `R-S6-grade-20261119-165820-bc3e46` trả PASS-VISIBLE. integrity, criteria, visible, regression và monitor đều đạt. Ma trận nguyên nhân × tầng của bộ ẩn chưa có dữ liệu để kết luận.
- Vòng 1 căn tham số theo tracking, giữ trần 2 lỗi/hãng/ngày và giảm 30 lỗi oan. Hai ca thiếu mã kiện vẫn sinh 10 lỗi oan và 270.000 đồng hoàn sai trên 5 seed.
- Report ghi được phép cân nhắc Tiếp tục vì số tổng đạt tiêu chí. Bàn giữ Cải tiến thêm dựa trên chi phí phân khúc chưa gắn kho và yêu cầu kiểm tuyến xử lý trực tiếp trước khi dùng thật.
- Chưa đo độ trễ cập nhật phân công tài xế theo chặng và thời gian xác minh mã kiện từ khách thật. Nếu cập nhật chậm hoặc quá SLA, số lỗi oan có thể vẫn xuất hiện và hàng chờ tăng; dùng kết quả diễn tập để chốt lại phạm vi.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Kênh CSKH có thể lấy mã kiện trước khi ghi tiền và tracking phản ánh đúng hãng, tài xế của chặng giao; khách chỉ biết mã đơn hoặc dữ liệu quét đến muộn có thể làm giả định này sai.
2. Cổng ngăn luồng tự động ghi tiền, ghi lỗi và báo hãng khi thiếu mã kiện mà có nhiều kiện đủ ngưỡng, như 10/60 lượt S6 đã chuyển duyệt; đối chiếu chỉ giảm rủi ro ngoài thực tế khi nguồn tracking có thể sai.
3. Trước Bước đánh giá 2, đo tỷ lệ thiếu mã kiện và lỗi còn lệch theo hãng/chặng, thời gian chờ p95 so với SLA 60 phút và chi phí luồng chưa rõ kho so với 10.000 đồng/ticket làm tay.
