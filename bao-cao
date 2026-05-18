# BÁO CÁO PHÂN TÍCH DỮ LIỆU: PHÁT HIỆN GIAN LẬN TÀI CHÍNH

## 1. Đặt vấn đề & Bài toán lựa chọn
* **Bài toán:** Phân tích dữ liệu giao dịch tài chính nhằm phát hiện các hành vi gian lận (Fraud Detection) hoặc giao dịch bất thường (Anomaly Detection).
* **Mục tiêu:** Sàng lọc ra các tài khoản và mã giao dịch có rủi ro cao dựa trên số tiền và tính minh bạch của thông tin giao dịch để kịp thời ngăn chặn.

## 2. Mô tả dữ liệu
Hệ thống kiểm thử sử dụng tập dữ liệu gồm 20 giao dịch tài chính (`bang_du_lieu_giao_dich.csv`) với các thuộc tính chính:
* `TransactionID`: Mã định danh giao dịch.
* `AccountID`: Mã tài khoản khách hàng.
* `Amount`: Số tiền giao dịch (USD).
* `Merchant`: Cửa hàng/Nền tảng thực hiện giao dịch.
* `TransactionType`: Hình thức (Thanh toán hoặc Chuyển khoản).
* `Location`: Thành phố diễn ra giao dịch.

## 3. Kết quả phân tích dữ liệu (Data Analytics)
Dựa trên thuật toán sàng lọc bằng thư viện `pandas` trong file `baitap.py`, kết quả thống kê hệ thống như sau:
* **Tổng số lượng giao dịch đã quét:** 20 giao dịch.
* **Tổng dòng tiền luân chuyển:** 500,200 USD.
* **Giá trị trung bình một giao dịch:** 25,010 USD.

## 4. Đánh giá kết quả & Phát hiện gian lận
Hệ thống phân tích đã khoanh vùng được **01 giao dịch siêu rủi ro** có dấu hiệu gian lận nghiêm trọng:

| STT | TransactionID | AccountID | Amount | Merchant | Location | Dấu hiệu vi phạm |
|---|---|---|---|---|---|---|
| 20 | **TX020** | ACC006 | **450,000 USD** | Unknown | Unknown | Số tiền vượt ngưỡng an toàn gấp 18 lần; Ẩn danh cửa hàng và vị trí giao dịch |

### Kiến nghị xử lý:
1. Tạm khóa ngay lập tức tài khoản `ACC006` để xác minh thông tin.
2. Đóng băng giao dịch mang mã hiệu `TX020` phục vụ công tác tra soát rủi ro.
