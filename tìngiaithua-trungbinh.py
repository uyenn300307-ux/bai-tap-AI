# =========================================================================
# BÀI 1: TÍNH GIAI THỪA CỦA MỘT SỐ NGUYÊN DƯƠNG (N!)
# =========================================================================
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua

# Thử nghiệm tính 5! (Kỳ vọng: 1 * 2 * 3 * 4 * 5 = 120)
so_n = 5
print(f"Bài 1: Giai thừa của {so_n} là: {tinh_giai_thua(so_n)}")
print("-" * 50)


# =========================================================================
# BÀI 2: TÍNH GIÁ TRỊ TRUNG BÌNH CỦA MỘT DÃY SỐ
# =========================================================================
def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    tong_so = sum(day_so)
    return tong_so / len(day_so)

# Thử nghiệm với một dãy số mẫu
cac_so = [10, 20, 30, 40, 50]
print(f"Bài 2: Giá trị trung bình của dãy số {cac_so} là: {tinh_trung_binh(cac_so)}")
print("-" * 50)


# =========================================================================
# BÀI 3: TÍNH LỢI NHUẬN SAU 12 THÁNG (LÃI KÉP)
# =========================================================================
def tinh_loi_nhuan(tien_goc, lai_suat_nam):
    # Lãi suất theo tháng = Lãi suất năm / 12 tháng
    lai_suat_thang = (lai_suat_nam / 100) / 12
    so_tien = tien_goc
    
    # Chạy vòng lặp tính tiền tích lũy qua từng tháng (12 tháng)
    for thang in range(1, 13):
        so_tien *= (1 + lai_suat_thang)
        
    loi_nhuan = so_tien - tien_goc
    return loi_nhuan, so_tien

# Thử nghiệm: Gửi 100,000,000đ với lãi suất 6% / năm
tien_dau_tu = 100000000
lai_suat = 6

tien_lai, tong_cuoi_ky = tinh_loi_nhuan(tien_dau_tu, lai_suat)
print("Bài 3: Kết quả tính toán đầu tư sau 12 tháng:")
print(f"  - Số tiền gốc ban đầu: {tien_dau_tu:,.0f} VND")
print(f"  - Tỷ lệ lãi suất: {lai_suat}% / năm")
print(f"  - Tiền lãi nhận được: {tien_lai:,.0f} VND")
print(f"  - Tổng số tiền nhận về: {tong_cuoi_ky:,.0f} VND")
