# Team

## Thông tin nhóm

- Tên nhóm: Aliba3
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Aliba3-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/griin-03/K5-L3B-DAY13-Aliba3-LaunchEconomics`, nhánh `main`, commit `b391a94`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Thanh Tùng | 2A202603819 | lethanhtung6803@gmail.com | griin-03 | Người viết code |
|   2 | Cấn Xuân Nghĩa | 2A202603818 | xuannghia2@gmail.com | xuannghia2 | Người kiểm số |
|   3 | Nguyễn Mạnh Hùng | 2A202603820 | hunglunnn@gmail.com | Hunglunnn | Người gắn nhãn 1 |
|   4 | Phạm Hoàng Huy | 2A202603821 | justcoffeee@gmail.com | justcoffeee | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Lê Thanh Tùng — 2A202603819

### Phần việc phụ trách

- Đảm nhiệm vai trò Người viết code chính: cài đặt môi trường, viết mã nguồn tính toán toàn diện trong `src/lab13.py` (Nhiệm vụ A, B, D, E).

### Đóng góp cụ thể

- Hoàn thiện ba hàm kinh tế chạy lại A1 vượt qua 100% ba phép thử chuẩn (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`).
- Xây dựng hàm `mo_hinh()` tính toán chi tiết chi phí từ trace cho 1.624 lượt chạy và 1.200 yêu cầu; lập trình mô phỏng 9 kịch bản phân tích độ nhạy B1, B2, B3 và B4.
- Lập trình tính toán cỡ mẫu thử nghiệm lâm sàng D1 theo phân phối chuẩn và phân tích thiết kế hiệu ứng cụm (Design Effect) với hệ số tương quan nội cụm ICC.
- Điền các kết quả tính toán định lượng vào `report/team/bang_chi_phi.md`.

### Bằng chứng

- File mã nguồn `src/lab13.py`.
- Dữ liệu kết quả tại `report/team/bang_chi_phi.md`.

## Cấn Xuân Nghĩa — 2A202603818

### Phần việc phụ trách

- Đảm nhiệm vai trò Người kiểm số: tính tay độc lập các số liệu để đối chiếu chéo với code; phụ trách tổng hợp kiểm toán chi phí cố định A4.

### Đóng góp cụ thể

- Tính toán thủ công kiểm chứng A1, A2 và xác nhận độ lệch không quá 0,1% so với mã nguồn.
- Kiểm tra tính nhất quán tuyến tính của mô hình trong Nhiệm vụ B (xác nhận kịch bản đổi cặp đúng bằng tổng các kịch bản riêng lẻ).
- Phối hợp xây dựng bảng kế hoạch pilot `report/team/pilot_plan.yaml`.

### Bằng chứng

- Các bảng số liệu kiểm chứng trong `report/team/bang_chi_phi.md` và `report/team/pilot_plan.yaml`.

## Nguyễn Mạnh Hùng — 2A202603820

### Phần việc phụ trách

- Đảm nhiệm vai trò Người gắn nhãn 1: thực hiện phân loại độc lập 20 ca lỗi theo chuẩn Google PAIR; phụ trách biên soạn đặc tả chỉ số telemetry E1.

### Đóng góp cụ thể

- Hoàn thành gắn nhãn độc lập 20 ca lỗi trong 8 phút không trao đổi, đạt tỷ lệ đồng thuận cao.
- Xây dựng danh mục 10 telemetry event chuẩn có thuộc tính `trace_id` tại `report/team/chi_so.md`.
- Viết báo cáo phân tích các chỉ số vận hành và kiểm tra chéo tính khả thi của các chỉ số đo lường.

### Bằng chứng

- Bảng nhãn Người 1 trong `report/team/bang_loi.md`.
- Bảng đặc tả event tại `report/team/chi_so.md`.

## Phạm Hoàng Huy — 2A202603821

### Phần việc phụ trách

- Đảm nhiệm vai trò Người gắn nhãn 2 kiêm Giữ hồ sơ: gắn nhãn độc lập 20 ca lỗi; khởi tạo và cập nhật xuyên suốt hồ sơ launch v0; điều phối duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Hoàn thành gắn nhãn độc lập 20 ca lỗi và cùng nhóm thảo luận thống nhất các quy tắc phân định lỗi gốc tại `report/team/bang_loi.md`.
- Trực tiếp soạn thảo và hoàn thiện hồ sơ launch 1 trang chuẩn mực tại `report/team/ho_so_launch_v0.md`.
- Điều phối phiên bảo vệ hồ sơ Gate 2a và hoàn thiện phiếu chấm phản biện tại `report/team/phieu_cham.md`.

### Bằng chứng

- Các tài liệu `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`.
