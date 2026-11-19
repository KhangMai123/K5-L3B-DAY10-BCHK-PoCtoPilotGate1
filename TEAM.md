# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): BCHK
- Lớp: `L3B`
- Repo của bàn: [K5-L3B-DAY10-BCHK-PoCtoPilotGate1](https://github.com/KhangMai123/K5-L3B-DAY10-BCHK-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
| 1 | Nguyễn Tấn Châu | 2A202603846 | Sản phẩm và kinh doanh | |
| 2 | Lê Quân Bảo | 2A202603888 | Vận hành và pháp lý | |
| 3 | Nguyễn Văn Hậu | 2A202603932 | Kỹ sư cổng và kiểm thử | |
| 4 | Mai Xuân Khang | 2A202603722 | Kỹ sư cổng và tích hợp | Có |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự điền đóng góp, bằng chứng và exit ticket của mình. Phần việc phụ trách ghi phạm vi phân công.

## NguyenTanChau-2A202603846

### Phần việc phụ trách

- GitHub `Lmeo2h`. Phụ trách mục tiêu, tiêu chí và quyết định chấp nhận ở A1, A3–A4, phối hợp A5.
- Phụ trách bản đồ dữ liệu B3, pre-mortem kinh doanh B6, cổng B7.4 và quyết định v1 B8. Giải thích ngưỡng chi phí, ROI, hoàn tiền và phạm vi pilot.

### Đóng góp cụ thể

- Tích hợp Phiếu A về mục tiêu, cách đo và tiêu chí chấp nhận vào nhánh cá nhân để nhóm đưa vào hồ sơ vòng 1.

### Bằng chứng

- Commit `624af09` bổ sung `templates/form-a-criteria.md`, được GitHub ghi nhận dưới tài khoản `chau2h`. Đối chiếu các mục A1–A5 với tiêu chí đã niêm phong tại `c3d3b19`.

### Exit ticket

- Bài học từ báo cáo: Một chỉ số chung đạt ngưỡng vẫn có thể che khuất vấn đề theo nhóm. Ở bộ nền after, chi phí chung là 4.456 đồng/ticket nhưng nhóm chưa xác định được kho tốn 10.359 đồng/ticket.
- Điều cần đo thêm: Chi phí và thời gian xử lý khi chuyển thẳng nhóm chưa rõ kho sang CSKH, cùng ảnh hưởng đến phạm vi và ROI của pilot.

### Công cụ hỗ trợ

- AI hỗ trợ

## LeQuanBao-2A202603888

### Phần việc phụ trách

- GitHub `LeBao403`. Phụ trách mục tiêu của kế toán và trưởng ca ở câu 1.2, telemetry production ở câu 1.4.
- Phụ trách HAZOP B4, checklist B5, pre-mortem vận hành và pháp lý B6, cấu hình `operations` và `legal`, runbook B7.5 và kế hoạch giờ cao điểm B7.6.

### Đóng góp cụ thể

- Tích hợp cấu hình vận hành, pháp lý và giới hạn kinh doanh cho cổng vòng 1 vào nhánh cá nhân để nhóm đưa vào bản chốt.

### Bằng chứng

- Commit `14edd87` bổ sung `config/operating_gates.json`. Các mốc người duyệt, công suất 6 ca/giờ, SLA 60 phút và giữ lỗi vượt trần được đối chiếu với Phiếu B B7.5–B7.6 và Phiếu C C11.
- Báo cáo S6 `R-S6-after-20261119-165820-bc3e46` ghi 3 ca/ngày vào hàng chờ, gồm cả kiểm mẫu, và 0 ca ùn trong mô phỏng.

### Exit ticket

- Bài học từ báo cáo: Cổng giữ lỗi vượt trần theo hãng có thể bảo vệ bên giao hàng mà vẫn cho phép ghi khoản hoàn hợp lệ. S6 cho thấy cần theo dõi riêng luồng đối soát lỗi và hàng chờ duyệt hoàn tiền.
- Điều cần đo thêm: Khả năng đáp ứng SLA khi nhiều yêu cầu thiếu mã kiện tới cùng lúc và thời gian bàn giao các ca ghi lỗi vượt trần cho người đối soát.

### Công cụ hỗ trợ

- AI hỗ trợ

## NguyenVanHau-2A202603932

### Phần việc phụ trách

- GitHub `common-maker`. Phụ trách thước đo offline ở câu 1.3, baseline B0–B1 và phân tích trace B2.
- Phối hợp triển khai cổng B7.1, đối chiếu hồi quy, thiết kế biện pháp chống rò rỉ dữ liệu đánh giá B7.2 và kiểm thử hành vi B7.3.

### Đóng góp cụ thể

- Tích hợp cổng vòng 1 và Phiếu B về đánh giá, phân tích trace, kiểm thử hành vi và quyết định v1 vào nhánh cá nhân.

### Bằng chứng

- Commit `7edb8ce` bổ sung `lab10/guards.py` và `templates/form-b-evaluation-gates.md`. Phiếu B B7.1–B7.3 ghi cách đối chiếu cổng, hồi quy và hai tình huống hành vi.
- Báo cáo hồi quy của nhóm `R-base-after-20261119-165819-bc3e46` đạt 110/110 lượt. Báo cáo S6 `R-S6-grade-20261119-165820-bc3e46` xác nhận không có ca mới hỏng trên bộ nền.

### Exit ticket

- Bài học từ trace: Cần kiểm tra từng bước ghi, gồm cả đúng kiện, đúng hãng và không có tác động khi chuyển duyệt. Một kết quả hoàn tiền đúng vẫn có thể đi kèm lỗi ghi nhầm hãng, như ở `S6-01@11` mốc base.
- Điều cần kiểm thêm: Các ca chưa thấy với mã kiện sai, dữ liệu chặng đến muộn hoặc nhiều yêu cầu đồng thời cho cùng một hãng.

### Công cụ hỗ trợ

- AI hỗ trợ

## MaiXuanKhang-2A202603722

### Phần việc phụ trách

- GitHub `KhangMai123`. Phụ trách repo và phân vai ở CP1, điều phối và rà soát tiêu chí ở CP2.
- Chủ trì B6, phụ trách `lab10/guards.py` ở B7.1, tích hợp cấu hình và tài liệu, đối chiếu kết quả đánh giá, kiểm hash bản chốt và tổng hợp v1 ở B8.
- Phụ trách tích hợp bản sửa S6, kiểm hồi quy và đối chiếu quyết định v2 với tiêu chí đã ký.

### Đóng góp cụ thể

- Tích hợp Phiếu A–B, tiêu chí và cổng vòng 1. Kiểm tra hash đã ký, so kết quả bộ nền trước và sau cổng, xác minh bản chốt và ghi quyết định v1.
- Với S6, bổ sung cổng chuyển duyệt trước khi ghi hoàn nếu thiếu mã kiện và có nhiều kiện đủ ngưỡng trễ. Giữ quy tắc gán lỗi theo tracking và trần lỗi theo hãng, đồng thời ghi dấu các ca vượt trần để đối soát.
- Bổ sung `carrier_parcel_mismatch_rate` và `ambiguous_parcel_handoff_rate`, kiểm hồi quy bộ nền, đối chiếu ba mốc S6 rồi hoàn thiện Phiếu C và gói nộp.

### Bằng chứng

- `c3d3b19` niêm phong tiêu chí; `fac3cfd` chứa bản chốt vòng 1 hash `1cccd450` và quyết định v1. Mốc nền `R-base-prepared-20261119-151949-84d2be` đạt 110/110 lượt.
- `b95a2b0` chứa bản sửa S6 và hồ sơ nộp. Báo cáo `R-S6-grade-20261119-165820-bc3e46` ghi `PASS-VISIBLE`: S6 after đạt 60/60 lượt, 0 lỗi hãng oan, 0 đồng hoàn sai và 0 lần lộ dữ liệu cá nhân.
- Kiểm hồi quy bộ nền `R-base-after-20261119-165819-bc3e46` đạt 110/110 lượt; bộ kiểm thử công khai đạt 13/13.

### Exit ticket

- Bài học: Độ trễ và quy trách nhiệm cần được xét theo từng kiện. Cổng vòng 1 giảm lỗi hãng oan từ 40 xuống 10; bước xác minh khi nhiều kiện đủ ngưỡng đưa 10 lượt còn lại sang người duyệt trước khi ghi.
- Điều còn chưa chắc: Tracking thật có cập nhật kịp hãng và tài xế ở từng chặng không, và việc xác minh mã kiện ảnh hưởng thế nào đến SLA 60 phút khi ca đến dồn.

### Công cụ hỗ trợ

- AI hỗ trợ
