# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Aliba3 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (toàn bộ 1.200 yêu cầu); 3.414 đ [simulated] (trong phạm vi noi_dia + hang_nang) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× mức 12.000 đ; phạm vi noi_dia: 0,22×, hang_nang: 0,69× [simulated] | Giả lập | Chuyên viên phân tích tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính chạy thử: 82,83%; Tỉ lệ bỏ qua: 27,12%; Mở lại 7 ngày: 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi đạt 100% đồng thuận; 5 giải pháp khắc phục có thước đo định lượng và vai trò chịu trách nhiệm | Xong, có bằng chứng | Trưởng nhóm QA |
| 6 · Pilot plan | Chia theo nhân viên (20 can thiệp vs 20 đối chứng); MDE = 0,06; n = 859 yêu cầu/nhóm; 3 luật dừng chuẩn NẾU-TRONG-THÌ-KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%); Xem lại 100%: 11.743 đ (0,98×) đến 12.415 đ (1,03×); Cố định: +2.370 đ/việc nếu khối lượng giảm 50% [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1:** Kỹ sư trưởng agent hoàn thành sửa khóa chống trùng lặp (idempotency key) và tích hợp cơ chế đối soát sổ cái kế toán tự động (xử lý dứt điểm ca lỗi 7, 20) trước ngày 15/12/2026.
- **Điều kiện 2:** Giám đốc vận hành ký biên bản chấp thuận mức chênh MDE = 0,06 (đánh đổi power đạt 0,64 nếu mức tác động thực tế chỉ là 0,05) trước ngày 18/12/2026.
- **Điều kiện 3:** Đội ngũ kỹ thuật kích hoạt đầy đủ 10 telemetry event chuẩn có thuộc tính `trace_id`; thay thế các chỉ số phút giả lập bằng dữ liệu đo thời gian thực tế ngay sau tuần rollout 0.10, hạn kiểm tra ngày 25/12/2026 bởi PM trợ lý hoàn phí.
- **Điều kiện 4:** Trưởng nhóm CSKH ban hành quy trình giảm tỷ lệ xem lại theo bậc dựa trên độ tin cậy của agent, tránh để tình trạng xem lại 100% kéo dài làm triệt tiêu hiệu quả kinh tế, hạn hoàn thành ngày 20/12/2026.
