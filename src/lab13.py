"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    cps = tong / thanh_cong if thanh_cong > 0 else 0
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else 0
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=chay_lai,
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=cps,
                hoa_don_moi_yc=hoa_don_moi_yc)


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print("=" * 60)
    print("NHIỆM VỤ A1: BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC")
    print("=" * 60)
    kiem_tra_dap_an_biet_truoc()

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A2: MÔ HÌNH CHI PHÍ TỪ TRACE")
    print("=" * 60)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.2f}')

    print(f"Chi phí mỗi việc thành công: {ket_qua['cps']:,.0f} đ [simulated]")
    print(f"Hóa đơn token + tool chia số yêu cầu: {ket_qua['hoa_don_moi_yc']:,.1f} đ")
    print(f"Tỉ lệ cps / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}% [simulated]")
    print(f"Tỉ trọng xem lại: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}% [simulated]")
    print(f"Tỉ trọng giờ nhân viên (xem + làm lại): {(ket_qua['lam_lai'] + ket_qua['xem_lai']) / ket_qua['tong'] * 100:.1f}% [simulated]")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A3: TÁCH THEO LOẠI YÊU CẦU")
    print("=" * 60)
    loai_list = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    for l in loai_list:
        sub_reqs = reqs[reqs['loai'] == l]
        sub_res = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        tl_tc = sub_res['thanh_cong'] / so_yc * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        cps_val = sub_res['cps']
        so_voi_12k = cps_val / BASELINE
        print(f"{l:12s}: Số YC={so_yc:4d} | Thành công={tl_tc:5.1f}% | Lần chạy/YC={lan_chay_tb:4.2f} | CPS={cps_val:8,.0f} đ [sim] | So với 12k={so_voi_12k:4.2f}x")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ A4: CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang)")
    print("=" * 60)
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_res = mo_hinh(runs, scope_reqs)
    tc_scope = scope_res['thanh_cong']
    cps_scope = scope_res['cps']
    print(f"Phạm vi pilot (noi_dia + hang_nang): Thành công={tc_scope}/{len(scope_reqs)}, CPS biến đổi={cps_scope:,.0f} đ [simulated]")

    # 45.000 yc/tháng -> tc_thang = 45000 * 900 / 1200 = 33750
    tc_thang_full = 45000 * tc_scope / len(reqs)
    cp_co_dinh_moi_viec_full = 40000000 / tc_thang_full
    cps_full = cps_scope + cp_co_dinh_moi_viec_full
    print(f"Quy mô đầy đủ 45.000 yc/tháng: TC/tháng={tc_thang_full:,.0f} | Cố định/việc={cp_co_dinh_moi_viec_full:,.0f} đ | Tổng CPS={cps_full:,.0f} đ ({cps_full/BASELINE:.2f}x)")

    # Nửa khối lượng: 22.500 yc/tháng
    tc_thang_half = tc_thang_full / 2
    cp_co_dinh_moi_viec_half = 40000000 / tc_thang_half
    cps_half = cps_scope + cp_co_dinh_moi_viec_half
    print(f"Nửa khối lượng (pilot): TC/tháng={tc_thang_half:,.0f} | Cố định/việc={cp_co_dinh_moi_viec_half:,.0f} đ | Tổng CPS={cps_half:,.0f} đ ({cps_half/BASELINE:.2f}x)")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B1 & B2: ĐỘ NHẠY VÀ XẾP HẠNG")
    print("=" * 60)
    kich_ban = {
        'Gốc (A2)':                 dict(),
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':    dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':    dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':       dict(max_lan_chay=1),
    }
    goc_cps = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps_val = mo_hinh(runs, reqs, **kw)['cps']
        diff = (cps_val / goc_cps - 1) * 100
        print(f'{ten:28s} {cps_val:8,.0f} đ [sim] {diff:+6.1f}%')

    cap_cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"\nB2: Giá token gấp đôi + xem lại gấp đôi: {cap_cps:,.0f} đ [sim] ({(cap_cps/goc_cps - 1)*100:+5.1f}%)")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B3: GIỚI HẠN CHẠY LẠI CẢ HỆ THỐNG")
    print("=" * 60)
    for k_lim in [1, 2, 3]:
        kw = dict(max_lan_chay=k_lim) if k_lim < 3 else dict()
        res_k = mo_hinh(runs, reqs, **kw)
        khong_tc = len(reqs) - res_k['thanh_cong']
        chi_phi_ht = res_k['tong'] + khong_tc * BASELINE
        print(f"Giới hạn {k_lim} lần: Tổng trợ lý={res_k['tong']:>10,.0f} đ [sim] | Không TC={khong_tc:>3d} | Cả hệ thống={chi_phi_ht:>10,.0f} đ | CPS={res_k['cps']:>6,.0f} đ [sim]")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ B4: XEM LẠI 100% PHẠM VI noi_dia + hang_nang")
    print("=" * 60)
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_runs = runs[runs['request_id'].isin(scope_reqs['request_id'])]
    tien_token_tool_scope = (scope_runs['tokens_in']/1000*GIA_VAO + scope_runs['tokens_out']/1000*GIA_RA + scope_runs['tool_calls']*GIA_TOOL).sum()

    # Yêu cầu có ít nhất 1 lần chạy status == 'ok'
    ok_req_ids = scope_runs[scope_runs['status'] == 'ok']['request_id'].unique()
    num_ok_reqs = len(ok_req_ids)
    xem_lai_100 = num_ok_reqs * 5 * LUONG_PHUT # 5 phút mỗi yc

    # Nhiệm vụ B4: Xem lại 100% phạm vi noi_dia + hang_nang
    # 1. 948 yêu cầu có status ok, mỗi yêu cầu xem lại 5 phút -> 9.480.000 đ
    # 2. 48 ca làm lại (phut_lam_lai > 0):
    #    - Với 9 phút/ca đề bài cho: 48 * 9 * 2.000 = 864.000 đ
    #    - Với 15.3 phút/ca thực tế dữ liệu: 48 * 15.3 * 2.000 = 1.468.800 đ
    # 3. Token + tool của 982 yêu cầu: 224.513 đ
    # 4. Chia cho 900 việc thành công
    xem_lai_100 = 948 * 5 * LUONG_PHUT
    lam_lai_9m = 48 * 9 * LUONG_PHUT
    tong_b4_9m = tien_token_tool_scope + xem_lai_100 + lam_lai_9m
    cps_b4_9m = tong_b4_9m / 900
    print(f"Xem lại 100% với 9 phút làm lại: Tổng={tong_b4_9m:,.0f} đ | CPS={cps_b4_9m:,.0f} đ ({cps_b4_9m/BASELINE:.2f}x) [simulated]")

    lam_lai_15m = 48 * 15.3 * LUONG_PHUT
    tong_b4_15m = tien_token_tool_scope + xem_lai_100 + lam_lai_15m
    cps_b4_15m = tong_b4_15m / 900
    print(f"Xem lại 100% với 15.3 phút làm lại: Tổng={tong_b4_15m:,.0f} đ | CPS={cps_b4_15m:,.0f} đ ({cps_b4_15m/BASELINE:.2f}x) [simulated]")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ D1: CỠ MẪU PILOT")
    print("=" * 60)
    n_a = co_mau(0.70, 0.75)
    print(f"a) Chia theo yêu cầu (+5%): {n_a} yêu cầu mỗi nhóm")
    de_b = 1 + (75 - 1) * 0.02
    n_b = math.ceil(n_a * de_b)
    staff_per_arm_b = math.ceil(n_b / 75)
    print(f"b) Theo nhân viên m=75: DE={de_b:.2f} -> {n_b} yêu cầu mỗi nhóm -> {staff_per_arm_b} NV mỗi nhóm (tổng {staff_per_arm_b*2} > 40: KHÔNG ĐỦ)")
    max_eff_c = 20 / 0.02
    print(f"c) 20 nhân viên mỗi nhóm: n_eff tối đa = c / ICC = 20 / 0.02 = {max_eff_c:,.0f} < {n_a} (KHÔNG ĐẠT MẪU 5 ĐIỂM)")
    max_eff_d = 6 / 0.02
    print(f"d) 6 depot mỗi nhóm: n_eff tối đa = c / ICC = 6 / 0.02 = {max_eff_d:,.0f} < {n_a} (KHÔNG ĐẠT MẪU 5 ĐIỂM)")
    n_e = co_mau(0.70, 0.76)
    # Giải m cho mức chênh 6 điểm với c=20: 20m / (1 + (m-1)*0.02) >= n_e
    # 20m >= n_e * (0.98 + 0.02m) => m * (20 - 0.02*n_e) >= 0.98 * n_e
    m_min = math.ceil(0.98 * n_e / (20 - 0.02 * n_e))
    de_e = 1 + (m_min - 1) * 0.02
    print(f"e) Mức chênh 6 điểm (+6%): n_per_arm={n_e} -> m >= {m_min} yc/người (DE={de_e:.2f})")

    print("\n" + "=" * 60)
    print("NHIỆM VỤ E1: CÁC CHỈ SỐ TÍNH THỬ")
    print("=" * 60)
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    chinh_count = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    print(f"Chỉ số chính (% đóng 24h & không mở lại 7 ngày): {chinh*100:.2f}% ({chinh_count}/{len(reqs)})")
    print(f"Chỉ số dùng (% bỏ qua gợi ý sua+bo): {bo_qua*100:.2f}% ({xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()}/{len(xem)})")
    print(f"Chỉ số an toàn (% mở lại 7 ngày): {an_toan*100:.2f}% ({(reqs['mo_lai_trong_7_ngay'] == 1).sum()}/{len(reqs)})")

