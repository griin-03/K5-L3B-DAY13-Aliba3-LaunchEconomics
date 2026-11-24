# Báo cáo cá nhân — LeThanhTung-2A202603819

## 1. Thông tin thành viên

- Họ tên: Lê Thanh Tùng
- MSSV: 2A202603819
- Email: lethanhtung6803@gmail.com
- Vai trong nhóm: Người viết code (Nhiệm vụ A, B, D, E)

## 2. Phần việc phụ trách

- Cài đặt và cấu hình môi trường thực thi Python cho nhóm trong thư mục `src/`.
- Lập trình toàn bộ mã nguồn tính toán kinh tế trong `src/lab13.py` bám sát các yêu cầu và công thức của Lab 13.
- Tính toán mô hình chi phí mỗi việc thành công từ trace thực tế (Nhiệm vụ A), phân tích độ nhạy 9 kịch bản và giới hạn chạy lại tối ưu (Nhiệm vụ B).
- Lập trình tính toán cỡ mẫu cho kế hoạch thử nghiệm pilot lâm sàng theo 3 cách phân cụm (Nhiệm vụ D).
- Đồng bộ hóa các kết quả tính toán định lượng vào bảng chi phí `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Triển khai thành công 3 hàm phân tích kinh tế chạy lại A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt chuẩn 100% 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
- Xây dựng hàm `mo_hinh()` xử lý 1.624 lượt chạy và 1.200 yêu cầu hoàn phí; tính toán chính xác chi phí mỗi việc thành công là 4.472 đ [simulated], chứng minh chi phí thực tế gấp 16,3 lần hóa đơn token thô do thời gian nhân viên chiếm tới 92,5%.
- Lập trình phân tích 4 phân khúc yêu cầu, chỉ ra `quoc_te` (22.515 đ = 1,88×) không khả thi để chạy agent, đề xuất thu hẹp phạm vi về `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×).
- Phân tích 9 kịch bản độ nhạy, chứng minh tác động tuyến tính của mô hình (B2) và chỉ ra giới hạn 2 lần chạy là rẻ nhất cho toàn công ty (6.901.220 đ [simulated]).
- Tính toán cỡ mẫu D1 chính xác theo công thức phân phối chuẩn `NormalDist().inv_cdf`, phân tích hệ số thiết kế Design Effect và chứng minh tính bất khả thi của việc chia theo depot do giới hạn trần $c / \text{ICC} = 300$.

## 4. Bằng chứng

- File mã nguồn `src/lab13.py` chạy hoàn hảo từ đầu đến cuối không lỗi.
- Bảng dữ liệu định lượng tại `report/team/bang_chi_phi.md`.
- Các tham số cỡ mẫu được nhúng vào `report/team/pilot_plan.yaml`.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity AI Assistant.
- Công việc: Hỗ trợ rà soát công thức tính Design Effect và giải phương trình tìm số lượng yêu cầu tối thiểu cho mỗi nhân viên $m \ge 299$ trong Nhiệm vụ D1.
- Kiểm tra kết quả: Tự viết script kiểm tra độc lập và đối chiếu với bảng số liệu chuẩn trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, đảm bảo độ sai lệch luôn nằm trong phạm vi cho phép dưới 0,5%.

## 6. Tự đánh giá

- Đạt 100% yêu cầu công việc được giao, hoàn thành đúng tiến độ và đảm bảo tính chính xác, trung thực tuyệt đối của số liệu.
