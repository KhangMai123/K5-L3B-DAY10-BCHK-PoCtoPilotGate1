# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** BCHK · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý yêu cầu giao trễ từ lúc nhận ticket đến khi hoàn và trả lời khách, với số tiền khớp sổ cái và chính sách hiệu lực, lỗi hãng có chứng cứ theo từng kiện, và ca cần phê duyệt được bàn giao trong SLA.

Tham chiếu nguyên tắc đối soát sổ cái, lấy điều kiện hoàn từ nguồn nghiệp vụ và chuyển người khi cần phê duyệt. Tài liệu Lab 9 là bản của trưởng nhóm và mô tả đánh giá bằng MockLLM trên dữ liệu giả lập. [PRD v1.1 Lab 9, §2, §3, §6](https://github.com/KhangMai123/K5-L3B-DAY09-MaiXuanKhang-2A202603722-EvaluationandFailureAnalysis/blob/dba4c3b21d19bb1591250bd81e9c46b928777880/docs/PRD_v1.1.md), [Eval card Lab 9](https://github.com/KhangMai123/K5-L3B-DAY09-MaiXuanKhang-2A202603722-EvaluationandFailureAnalysis/blob/dba4c3b21d19bb1591250bd81e9c46b928777880/docs/eval_card.md).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Nối được khoản hoàn, bên chịu tiền và lỗi hãng với đúng đơn, kiện và căn cứ, để tìm và điều chỉnh chênh lệch trước kỳ đối soát tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Nhận được ca vượt hạn mức hoặc thiếu căn cứ trong 60 phút, kèm lý do, dữ kiện tracking và phiên bản chính sách đủ để ra quyết định.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn bản ghi phê duyệt cho đề xuất hoàn trên hạn mức tự động. | Phát hành thông báo ghi lỗi cho hãng vận chuyển. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ lượt chọn phê duyệt có kết quả đúng, tính theo %. | Tỷ lệ thông báo lỗi hãng có căn cứ tracking sai hoặc thiếu, tính theo %, kèm số thông báo bị gắn cờ. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Xét 22 ticket × 5 seed bộ nền. Trưởng ca CSKH gán tập mã phê duyệt hợp lệ cho từng lượt đủ điều kiện dựa trên bảng `approvals`, đơn, khách, ticket, chính sách theo `as_of` và số tiền đề xuất. Một mã hợp lệ phải khớp cả ba định danh, do người có quyền duyệt, còn hạn, có `status=valid` và đủ `max_vnd`. Đọc kết quả chọn ở `approval_used` hoặc kết quả bàn giao trong trace. | Log gửi hãng đã khử lặp theo ID gửi, bản ghi lỗi và snapshot tracking của đúng kiện tại lúc ghi. Đối chiếu bản chính sách hiệu lực theo thời điểm đó. Tín hiệu đến từ các bản ghi giao dịch, không cần nhãn đánh giá. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Mẫu số là số lượt có đề xuất hoàn trên hạn mức theo chính sách hiệu lực và đủ dữ liệu để xác lập nhãn, kể cả lượt thiếu log chọn. Tử số là lượt chọn mã thuộc tập hợp lệ, hoặc chuyển duyệt mà chưa ghi tiền khi tập hợp lệ rỗng. Thiếu log kết quả thì tính sai. Thiếu snapshot để xác lập nhãn thì tách số lượt chưa chấm khỏi mẫu số và báo tỷ lệ phủ nhãn. Mẫu số bằng 0 thì ghi không có dữ liệu. | Chia số thông báo có ít nhất một lỗi đối chiếu cho tổng số thông báo lỗi hãng đã gửi trong kỳ. Gắn cờ nếu thiếu bản ghi để nối, sai mã hãng, hoặc độ trễ và nguyên nhân của kiện không đủ điều kiện theo chính sách hiệu lực. Theo dõi số thiếu dữ liệu riêng. Mẫu số bằng 0 thì ghi không có dữ liệu. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Tính trên cửa sổ trượt 60 phút và cập nhật khi có thông báo mới. Từ một thông báo bị gắn cờ, Tùng tạm ngưng ghi lỗi và báo hãng ở luồng tự động liên quan, giao Hạnh đối chiếu tracking và Oanh rà soát khoản phạt trước khi tiếp tục. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Bước chọn vẫn có thể đúng khi số tiền đề xuất sai, hoặc mã hợp lệ bị dùng lại khi ghi. | Tracking có thể sai hoặc chứa nguyên nhân nhập nhầm mà các nguồn vẫn khớp nhau. Tín hiệu cũng bỏ sót lỗi hãng chưa phát thông báo và dữ liệu cá nhân trong nội dung. |

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Y đạt 1,0 (50/50), nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X có 49/50 lượt đúng (0,9800), nên số minh họa chưa đủ để kết luận Y tốt hơn X có ý nghĩa thống kê.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ lượt đúng trên bộ thử bắt buộc của mốc quyết định thấp hơn 97% thì chúng tôi sẽ khoanh nhóm lỗi và cải tiến thêm, hoặc thu hẹp nếu đo lại xác nhận phần giữ đạt ngưỡng. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đúng cả năm seed thấp hơn 85% thì chúng tôi sẽ giữ xử lý tay để kiểm tra sai khác theo seed. | Nếu tỷ lệ ticket đúng cả năm seed thấp hơn 91% thì chúng tôi sẽ giữ xử lý tay để khắc phục thiếu ổn định, hoặc thu hẹp sau khi xác nhận phần giữ đạt ngưỡng. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bất kỳ bộ thử bắt buộc nào vượt 0 đồng thì chúng tôi sẽ giữ pilot chưa mở, đối chiếu từng bút toán và chặn nguyên nhân trước khi đo lại. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi hãng oan trên bất kỳ bộ thử bắt buộc nào vượt 0 thì chúng tôi sẽ giữ pilot chưa mở và đối chiếu lỗi theo kiện, hãng, nguyên nhân và chính sách hiệu lực. | |
| `pii_leaks_max` | Nếu số thông báo hãng làm lộ dữ liệu cá nhân trên bất kỳ bộ thử bắt buộc nào vượt 0 thì chúng tôi sẽ giữ pilot chưa mở, khoanh luồng gửi và kiểm tra bản ghi outbound. | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người duyệt trên bộ thử vượt 25% thì chúng tôi sẽ phân tích lý do chuyển và kiểm tra công suất trước khi chọn phạm vi. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: Cấm gửi sang hãng họ tên, số điện thoại, địa chỉ đường phố, thông tin liên hệ người nhận hoặc nguyên văn ghi chú khách.
- Ngưỡng chuyển cho người duyệt: Chuyển Hạnh trước khi ghi nếu khoản hoàn vượt hạn mức tự động của chính sách hiệu lực hoặc đưa tổng hoàn tự động của khách vượt 300.000 đồng/ngày mà chưa có phê duyệt hợp lệ cho ca đó. Chuyển duyệt cả khi lần ghi làm vượt trần hoàn tự động cả ngày.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có khi đọc cùng nhau. Tỷ lệ đúng và ổn định bảo vệ khách, số lỗi oan và lộ dữ liệu bảo vệ hãng và người nhận, còn thời gian chờ, đối soát và chi phí phản ánh phần việc của trưởng ca, kế toán và shop. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép giảm chuyển người có thể ghi tiền hoặc phạt hãng khi thiếu chứng cứ. Chuyển tất cả sẽ làm khách chờ và dồn việc cho ca trực. Đọc tỷ lệ chuyển cùng số ca ùn và ba chỉ số an toàn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có nếu ca đúng được giải quyết, ca ngoại lệ tới người có quyền, tài chính đối soát được và tác hại không phát sinh. Một ca quá 60 phút hoặc một vi phạm an toàn kích hoạt dừng theo quy tắc bên dưới. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Giữ mức 0 cho hoàn sai, lỗi hãng oan, lộ dữ liệu. Đo lại theo kho, hãng, chính sách và giờ cao điểm để đặt lại sàn chất lượng, tỷ lệ bàn giao và ngưỡng chi phí, ROI trên bản tiêu chí mới. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Chọn 97% cho `pass_rate` và phiên bản 2 (91%) cho `pass_k`. Với thiết kế 22 ticket × 5 seed, cần ít nhất 107/110 lượt đúng và 21/22 ticket đúng cả năm seed. Sàn theo ticket hạn chế nhóm khách gặp kết quả thất thường. `pass_rate` đếm từng lượt; `pass^k` đếm ticket đúng tất cả các lượt; `pass@k` đếm ticket có ít nhất một lượt đúng.
- Chọn tỷ lệ chuyển duyệt 25% làm mốc rà soát tải người. Với chi phí duyệt 10.000 đồng/ca, tỷ lệ này dành khoảng 2.500 đồng công duyệt cho mỗi ticket trước kiểm mẫu và phí trực.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 7.800 đồng · `roi_min` 0,25 · `queue_stuck_max` 0.
- Mức 7.800 đồng dành ít nhất 2.200 đồng/ticket chênh lệch chi phí so với làm tay 10.000 đồng. ROI tối thiểu 25% yêu cầu mỗi đồng chi phí pilot mang lại ít nhất 0,25 đồng tiết kiệm ròng sau tiền hoàn sai; báo cáo tính theo tổng chi phí máy, công duyệt và phí trực. Sức duyệt chuẩn là 6 ca/giờ/người, ca 480 phút, phí trực 30.000 đồng/người/ca. Không chấp nhận ca ùn theo SLA 60 phút.
- Trần cứng từ `ops_limits`: 2.000.000 đồng hoàn tự động/ngày, 300.000 đồng/khách/ngày, 2 lỗi tự động/hãng/ngày và 1.500 đồng tiền máy/ticket. Căn cứ định lượng lấy từ `data/world.json`.
- Điều kiện dừng. Tạm dừng các thao tác tự động liên quan ngay khi xác nhận hoàn sai, ghi lỗi hãng oan, lộ dữ liệu cá nhân hoặc đã ghi khoản hoàn cần duyệt mà thiếu phê duyệt hợp lệ. Tạm dừng nhận mới vào pilot nếu có ca ùn, có ca chờ quá 60 phút hoặc tổng hoàn tự động chạm trần ngày. Chuyển ca sang xử lý tay và chỉ mở lại sau đối soát, xử lý hàng chờ và phê duyệt của giám sát vận hành.
- Quy tắc quyết định áp dụng trên các bộ thử bắt buộc của từng mốc. V1 dùng bộ nền, v2 sẽ áp dụng cả gói thử sự cố được cấp.
  - **Tiếp tục.** Trên tất cả bộ thử bắt buộc ở mốc quyết định, đủ năm chỉ số bắt buộc và các ngưỡng đã ký, không có dòng vượt trần vận hành, kinh doanh hay pháp lý. Chỉ tiếp tục trong phạm vi đã đo.
  - **Thu hẹp.** Ba ngưỡng an toàn đều đạt, có thể cô lập phần trượt chất lượng hoặc kinh doanh, vận hành theo kho hoặc loại ca, và đo lại chứng minh phần giữ lại khác rỗng đạt các ngưỡng. Phần bị cắt chuyển xử lý tay.
  - **Cải tiến thêm.** Còn vi phạm an toàn hoặc có chỉ số chưa đạt mà chưa chứng minh được phạm vi thu hẹp an toàn. Giữ xử lý tay, chỉ định người sửa, giả thuyết và hạn đo lại trước khi mở pilot.
  - **Dừng.** Dừng pilot nếu chưa thể khoanh và đối soát tác hại đã xác nhận, hoặc đã qua một vòng khắc phục theo hạn mà vẫn còn vi phạm an toàn hoặc không có phạm vi nào vận hành được trong trần ngân sách và SLA.
- Ngày xem lại tiêu chí: `2026-11-20` · Ai dự: Nguyễn Tấn Châu, Lê Quân Bảo, Nguyễn Văn Hậu và Mai Xuân Khang (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T15:02:43` (UTC+7) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `c3d3b19` |
| Đã push lên `origin main` thành công? | [Commit ký tiêu chí trên GitHub](https://github.com/KhangMai123/K5-L3B-DAY10-BCHK-PoCtoPilotGate1/commit/c3d3b19bbc35c449dc203685ce985c5bcce7f5ed) |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
