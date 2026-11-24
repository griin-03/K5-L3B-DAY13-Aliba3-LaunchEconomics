# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Aliba3
- Lớp: L3B
- Thành viên: xem `TEAM.md` (Lê Thanh Tùng, Cấn Xuân Nghĩa, Nguyễn Mạnh Hùng, Phạm Hoàng Huy)

## 2. Mục tiêu và cách tiếp cận

- Mục tiêu: Xây dựng hồ sơ launch v0 toàn diện cho trợ lý hoàn phí LogiX-VN bảo vệ tại cổng Gate 2a, trả lời 4 câu hỏi cốt lõi: (1) Tính kinh tế thật sự của agent; (2) Hành vi sử dụng và đo lường qua telemetry; (3) Phân loại lỗi và cơ chế khắc phục rủi ro; (4) Thiết kế thử nghiệm pilot khoa học, tách được tác động và có điều kiện dừng an toàn.
- Cách tiếp cận: Phân tích dữ liệu thực tế từ 1.624 lần chạy và 1.200 yêu cầu hoàn phí; mô hình hóa chi phí toàn diện (tính cả chi phí token, tool, thời gian nhân viên xem lại và làm lại); kiểm định độ nhạy; phân loại lỗi theo chuẩn Google PAIR; và tính toán cỡ mẫu thử nghiệm lâm sàng theo thống kê chuẩn tắc.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Viết mã nguồn mô phỏng chi phí trong `src/lab13.py` và tổng hợp tại `report/team/bang_chi_phi.md`. Tính toán chi phí thực tế cho mỗi việc thành công đạt 4.472 đ [simulated], gấp 16,3 lần hóa đơn token thô do chi phí nhân viên xem lại và làm lại chiếm tới 92,5%. Phân tích chi tiết 4 phân khúc cho thấy `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×) là hai nhóm đem lại hiệu quả vượt trội so với mức baseline 12.000 đ.
- **Nhiệm vụ B (Phân tích độ nhạy):** Khảo sát 9 kịch bản biến động đơn lẻ và đa biến. Xác định 3 yếu tố nhạy cảm nhất là: (1) Số ca làm lại (+51,8%); (2) Tỉ lệ xem lại (+40,7%); (3) Lương nhân viên (+23,1%). Chứng minh giới hạn 2 lần chạy là tối ưu cho toàn hệ thống công ty (6.901.220 đ [simulated]) và phân tích rủi ro xem lại 100% (chi phí đội lên 11.743 đ - 12.415 đ [simulated], triệt tiêu lợi ích kinh tế).
- **Nhiệm vụ C (Bảng lỗi PAIR):** Gắn nhãn độc lập 20 ca lỗi với tỷ lệ đồng thuận 100% giữa 2 chuyên viên đánh giá; thiết lập quy tắc phân định rõ ràng giữa lỗi gốc và giải pháp; đề xuất 5 giải pháp khắc phục chi tiết có chỉ số đo lường định lượng và vai trò chịu trách nhiệm tại `report/team/bang_loi.md`.
- **Nhiệm vụ D (Kế hoạch pilot):** Xây dựng kế hoạch thử nghiệm pilot chi tiết tại `report/team/pilot_plan.yaml`. Lựa chọn phương án phân cụm theo nhân viên (20 can thiệp vs 20 đối chứng) tại 12 depot; phân tích năng lực kiểm định và chấp nhận MDE = 0,06 (n = 859 yêu cầu/nhóm); thiết lập 3 luật dừng nghiêm ngặt theo mẫu NẾU-TRONG-THÌ-KHÔNG THÌ.
- **Nhiệm vụ E (Chỉ số & Hồ sơ Launch v0):** Hoàn thiện tài liệu đặc tả 10 telemetry event chuẩn có `trace_id` tại `report/team/chi_so.md`, phân tích rủi ro kinh tế và đóng gói hồ sơ launch 1 trang tại `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

- Chi phí mỗi việc thành công trong phạm vi pilot (`noi_dia` + `hang_nang`): **3.414 đ [simulated]** (chưa cố định) và **4.599 đ [simulated]** (đã gồm chi phí cố định 40 triệu đ/tháng ở quy mô 45.000 yêu cầu), tiết kiệm 62% chi phí so với nhân viên tự làm (12.000 đ).
- Chỉ số vận hành thử nghiệm: Tỷ lệ thành công 81,5% (978/1.200); Tỷ lệ đóng 24h & không mở lại 7 ngày đạt 82,83%; Tỷ lệ mở lại 7 ngày là 4,25%.
- Đề xuất cuối cùng: **Go có điều kiện** cho thử nghiệm pilot phân tầng theo nhân viên trong phạm vi `noi_dia` và `hang_nang`.
- Kết quả duyệt chéo Gate 2a: Nhận đánh giá **30/30 điểm** từ Hội đồng phản biện với sự nhất trí cao về tính trung thực dữ liệu, tính chặt chẽ trong thiết kế thử nghiệm và việc chủ động nhận diện con số bất lợi.

## 5. Khó khăn và cách xử lý

- *Khó khăn:* Dữ liệu thời gian xem lại và làm lại là dữ liệu giả lập (`_simulated`), có nguy cơ dẫn tới ngộ nhận về tính khả thi nếu áp dụng trực tiếp vào thực tế.
- *Cách xử lý:* Tuân thủ nghiêm ngặt quy tắc gắn nhãn `[simulated]` trên toàn bộ báo cáo, đồng thời thiết kế điều kiện tiên quyết trong hồ sơ launch: bắt buộc phải thay thế các tham số giả lập bằng số đo thời gian thực tế ngay sau tuần triển khai rollout đầu tiên.
- *Khó khăn:* Số lượng nhân sự CSKH của công ty chỉ có 40 người, không đủ cỡ mẫu thống kê để phát hiện mức chênh lệch 5 điểm phần trăm với power 0,80.
- *Cách xử lý:* Phân tích toán học minh bạch, lượng hóa mức đánh đổi MDE = 0,06 (yêu cầu mỗi nhân viên xử lý ≥ 299 đơn, DE = 6,96) và yêu cầu Giám đốc vận hành ký phê duyệt đánh đổi trước khi triển khai.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- *Hạn chế:* Chưa tính đến tác động tâm lý hoặc sự ỷ lại của nhân viên vào trợ lý ảo khi tỷ lệ gợi ý đúng kéo dài.
- *Hướng cải thiện:* Trong các đợt mở rộng tiếp theo, cần bổ sung bài kiểm tra mù (blind review) định kỳ hàng tháng để đánh giá khách quan kỹ năng nghiệp vụ của đội ngũ CSKH khi có và không có trợ lý hỗ trợ.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*.
- Tài liệu thư viện `statsmodels` (phân hệ `statsmodels.stats.power.NormalIndPower`).
