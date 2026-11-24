# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng | % yêu cầu thuộc nhóm can thiệp được nhân viên mở bằng trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia tổng yêu cầu nhóm can thiệp | Không cần tính (đề xuất đo trong pilot) |
| An toàn | % đơn hoàn sai số tiền phát hiện qua kiểm tra mẫu hàng tuần | Số đơn kiểm tra mẫu có số tiền hoàn thực tế lệch số tiền đúng, chia số đơn kiểm tra | Không cần tính (bắt lỗi ngầm như ca 5, 17) |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Ứng dụng khách hàng | request_id, loai, so_tien, arm, trace_id | Khi khách hàng gửi yêu cầu hoàn phí |
| agent_run_completed | Trợ lý hoàn phí (Agent) | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần agent hoàn thành một lượt chạy (kể cả lỗi) |
| agent_suggestion_shown | Giao diện CSKH | staff_id, so_tien_de_xuat, trace_id | Khi bảng gợi ý quyết định hiển thị cho nhân viên |
| staff_review_decision | Nhân viên CSKH | quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id | Khi nhân viên xác nhận duyệt, chỉnh sửa hoặc hủy bỏ |
| staff_rework_completed | Nhân viên CSKH | phut_lam_lai, ly_do, trace_id | Khi nhân viên hoàn thành xử lý thủ công lại yêu cầu |
| refund_ledger_write | Dịch vụ sổ cái kế toán | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi nhận hoàn tiền vào sổ cái kế toán |
| handoff_to_staff | Trợ lý hoàn phí (Agent) | reason, tom_tat, trace_id | Khi agent chủ động chuyển yêu cầu cho nhân viên |
| ticket_closed | Hệ thống quản lý ticket | closed_at, trace_id | Khi ticket hoàn tất đóng |
| ticket_reopened | Khách hàng | reopened_at, reason, trace_id | Khi khách hàng mở lại khiếu nại trong vòng 7 ngày |
| audit_sample_checked | Bộ phận Kế toán / Kiểm soát | so_tien_da_hoan, so_tien_chuan, trace_id | Khi hoàn thành kiểm toán mẫu hàng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h và không mở lại 7 ngày):** Tính từ mốc thời gian giữa `refund_request_created` và `ticket_closed` (hiệu số ≤ 24 giờ), đồng thời không xuất hiện event `ticket_reopened` có cùng `trace_id` trong vòng 7 ngày.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm các event `staff_review_decision` có thuộc tính `quyet_dinh` là `sua` hoặc `bo`, chia cho tổng số event `staff_review_decision`.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm số `trace_id` có phát sinh event `ticket_reopened` trong vòng 7 ngày kể từ khi có `ticket_closed`, chia cho tổng số `trace_id` có `refund_request_created`.
- **Chỉ số dùng đề xuất (% yêu cầu mở bằng trợ lý):** Đếm số `trace_id` có event `agent_suggestion_shown`, chia cho tổng số `trace_id` thuộc nhóm can thiệp (`arm == intervention`) trong event `refund_request_created`.
- **Chỉ số an toàn đề xuất (% đơn hoàn sai tiền kiểm toán):** Đếm số event `audit_sample_checked` có `so_tien_da_hoan != so_tien_chuan`, chia cho tổng số event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ yêu cầu cần làm lại theo tuần vượt quá 7% (đợt chạy thử: 4,9% trong phạm vi pilot) | Thu hẹp phạm vi chỉ xử lý `noi_dia`, rà soát nguyên nhân gốc của 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% | Chi phí lên tới 11.743 đ = 0,98× (hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút như thực tế trace) [simulated], triệt tiêu lợi ích kinh tế | Tỉ lệ yêu cầu phải xem lại vẫn ở mức > 50% khi kết thúc giai đoạn rollout 0.25 | Giảm dần tỷ lệ xem lại theo bậc dựa trên độ tin cậy khi tỉ lệ sửa/bỏ giảm xuống dưới 15% | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm tăng thêm 1.185 đ/việc ở mức 45.000 yc/tháng và tăng 2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số việc thành công thực tế đạt dưới 50% kế hoạch tuần liên tiếp | Tạm dừng mở rộng quy mô pilot, đàm phán lại chi phí cố định với nhà cung cấp nền tảng | PM trợ lý hoàn phí |
