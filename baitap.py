import pandas as pd

# 1. Tạo dữ liệu mẫu từ hình ảnh
data = {
    "STT": list(range(1, 21)),
    "Timestamp": [
        "2026-01-01 08:15", "2026-01-01 09:20", "2026-01-01 10:05", "2026-01-01 11:30",
        "2026-01-01 12:10", "2026-01-01 13:45", "2026-01-01 14:20", "2026-01-01 15:00",
        "2026-01-01 16:30", "2026-01-01 17:10", "2026-01-01 18:00", "2026-01-01 19:15",
        "2026-01-01 20:30", "2026-01-01 21:00", "2026-01-01 22:10", "2026-01-02 08:20",
        "2026-01-02 09:40", "2026-01-02 10:15", "2026-01-02 11:50", "2026-01-02 12:30"
    ],
    "TransactionID": [f"TX{i:03d}" for i in range(1, 21)],
    "AccountID": [
        "ACC001", "ACC002", "ACC003", "ACC001", "ACC004", "ACC002", "ACC005", "ACC003",
        "ACC006", "ACC004", "ACC007", "ACC008", "ACC009", "ACC010", "ACC001", "ACC002",
        "ACC003", "ACC004", "ACC005", "ACC006"
    ],
    "Amount": [
        2500, 3200, 1800, 2750, 3500, 4100, 2900, 3300, 2700, 3900,
        3000, 2800, 2600, 3100, 2950, 3400, 2200, 3600, 2800, 450000
    ],
    "Merchant": [
        "Amazon", "Shopee", "Lazada", "Grab", "Tiki", "Amazon", "Shopee", "Grab",
        "Tiki", "Lazada", "Amazon", "Shopee", "Grab", "Tiki", "Lazada", "Amazon",
        "Shopee", "Grab", "Tiki", "Unknown"
    ],
    "TransactionType": [
        "Payment", "Payment", "Payment", "Transfer", "Payment", "Transfer", "Payment", "Transfer",
        "Payment", "Transfer", "Payment", "Payment", "Transfer", "Payment", "Transfer", "Payment",
        "Payment", "Transfer", "Payment", "Transfer"
    ],
    "Location": [
        "Hanoi", "HCM", "Danang", "Hanoi", "CanTho", "HCM", "Haiphong", "Danang",
        "Hanoi", "HCM", "Danang", "CanTho", "Hanoi", "HCM", "Haiphong", "Hanoi",
        "HCM", "Danang", "CanTho", "Unknown"
    ]
}

# 2. Chuyển thành bảng dữ liệu (DataFrame)
df = pd.DataFrame(data)

# 3. Xuất thành file .csv nằm cùng thư mục với file code này
df.to_csv("bang_du_lieu_giao_dich.csv", index=False, encoding='utf-8-sig')

print("Đã xuất file 'bang_du_lieu_giao_dich.csv' thành công!")
