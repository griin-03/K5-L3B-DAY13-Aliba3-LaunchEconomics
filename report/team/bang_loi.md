# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lê Thanh Tùng · Người gắn nhãn 2: Cấn Xuân Nghĩa (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6, 9 (Do người dùng vs Hệ thống):** Gốc lỗi là khách nhập sai mã hoặc chọn sai mục; việc agent không gợi ý là cải tiến ở giải pháp khắc phục chứ không phải lỗi thiết kế ban đầu.
- **Ca 13 (Giới hạn hệ thống vs Hệ thống):** Yêu cầu nằm ngoài phạm vi chính sách hiện hành thì là Giới hạn hệ thống, kể cả khi agent xử lý câu trả lời từ chối chưa khéo léo.
- **Ca 8, 15 (Hệ thống vs Ngầm):** Sai sót đã lộ ra ngay trên giao diện hoặc bị nhân viên phát hiện trực tiếp khi xử lý, không phải lỗi ngầm.
- **Ca 18 (Ngữ cảnh vs Hệ thống):** Số tiền hoàn tính đúng 100% theo công thức chính sách, chỉ giả định "khách hàng tự hiểu cách tính chia đôi" là không khớp ngữ cảnh giao tiếp.
- **Ca 12 (Ngầm vs Hệ thống):** Kết quả trả về cho khách vẫn đúng nhưng chi phí token/tool bị đội gấp 3 lần suốt 3 tuần mà không ai phát hiện; đây là lỗi ngầm về mặt kinh tế vận hành.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ vượt quá 2% số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT và tự động tra sang mã vận đơn nội bộ; nếu không tra được thì hiển thị hướng dẫn kèm ảnh chụp mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng kích hoạt: > 0 ca | Chỉ phát thông báo "đã hoàn" khi dịch vụ sổ cái xác nhận `ok`; nếu gặp lỗi 503 sau 3 lần thử lại thì chuyển trạng thái "đang xử lý" và giao nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi tỉ lệ khiếu nại mở lại do thắc mắc số tiền nhưng kiểm tra thấy tính đúng, tổng hợp theo tuần | Mẫu tin nhắn gửi khách luôn ghi chi tiết công thức tính: ví dụ "Cước phí 30.000 đ × tỉ lệ hỗ trợ 50% = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `thieu_du_lieu`, phân loại theo nhóm yêu cầu theo tuần | Giữ cơ chế chuyển tiếp nhân viên kèm bản tóm tắt tự động; loại bỏ hoàn toàn nhóm `quoc_te` ra khỏi phạm vi thử nghiệm pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá cước hiện hành; ngưỡng cảnh báo: > 1% đơn có chênh lệch | Tự động làm mới bộ nhớ đệm (cache) ngay khi cập nhật bảng giá cước mới; ghi rõ phiên bản bảng giá vào thuộc tính của trace | Kế toán trưởng |
