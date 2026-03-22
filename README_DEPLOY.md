# HƯỚNG DẪN ĐẨY WEBSITE HỆ THỐNG KTX LÊN MẠNG ONLINE MIỄN PHÍ

Một Website gồm có 2 phần: **Database** (Cơ sở dữ liệu lưu thông tin) và **Source Code Web** (Giao diện và Code Python chạy Server).
Chúc mừng bạn vì Database của bạn đã nằm sẵn trên Internet (nền tảng Aiven) chứ không nằm trên ổ cứng Local. Nên việc Deploy bây giờ **Cực Kỳ Đơn Giản**!

Ta sẽ sử dụng nền tảng **Render (render.com)** vì nó hiện đại, hỗ trợ Python Flask miễn phí và rất mạnh mẽ.

## Bước 1: Chuẩn bị Source Code lên GitHub
Render.com nhận mã nguồn của bạn thông qua nền tảng trung gian GitHub. Bạn cần tạo 1 kho chứa.
1. Truy cập [GitHub](https://github.com/) và tạo / đăng nhập một tài khoản miễn phí.
2. Bấm nút **[+] -> New repository** ở góc trên cùng bên phải.
3. Đặt tên Repo là `ktx-baohong-app` (hoặc tùy ý), chọn **Private** hoặc **Public**, rồi nhấn **Create repository**.
4. Mở cửa sổ Terminal (hoặc Git Bash) *ngay bên trong thư mục `d:\TTCN_BaoHongKTX`* của bạn và gõ lần lượt các lệnh này để đẩy code lên kho (Nhớ thay đường link https của bạn vào):
   ```bash
   git init
   git add .
   git commit -m "Khoi tao du an KTX"
   git branch -M main
   git remote add origin https://github.com/TênTàiKhoản/ktx-baohong-app.git
   git push -u origin main
   ```
*(Lưu ý: Nếu màn hình máy tính của bạn báo lỗi: **git : The term 'git' is not recognized**, có nghĩa là máy bạn chưa cài phần mềm Git. Đừng lo, bạn có 2 cách để giải quyết:)*

### Cách 1 (Dành cho Dân IT): Cài phần mềm Git
1. Tải và cài đặt phần mềm Git tại đây: **[https://git-scm.com/downloads](https://git-scm.com/downloads)** (Cứ bấm Next liên tục để cài)
2. Tắt phần mềm Code (VSCode/PyCharm) đi rồi mở lại để nhận lệnh Git.
3. Gõ lại từ lệnh `git init` trở đi như bên trên.

### Cách 2 (Siêu dễ, AI cũng làm được): Kéo thả thư mục (Không cần lệnh)
1. Mở thư mục `d:\TTCN_BaoHongKTX` của dự án trên máy tính của bạn.
2. Trên kho GitHub vừa tạo ở trình duyệt, ở giữa màn hình bạn sẽ thấy luồng chữ nhỏ: **"uploading an existing file"**. Hãy bấm vào chữ xanh đó.
3. Một bảng Kéo-Thả to đùng sẽ hiện ra. Bạn **Chọn tất cả** các file trong máy tính (ngoại trừ thư mục `.venv` nặng và `__pycache__`) rồi kéo thẳng thả vào trình duyệt.
4. Đợi web load xong, Kéo xuống dưới cùng và nhấn nút xanh lá **Commit changes**.

---

## Bước 2: Liên kết GitHub với Render
Bây giờ ta sẽ tạo Máy chủ ảo (Web Service) để chạy code Python 24/7.
1. Truy cập [Render.com](https://render.com/) và đăng ký bằng chính tài khoản GitHub vừa tạo.
2. Tại màn hình Dashboard, bấm **New +** -> Chọn **Web Service**.
3. Chọn tuỳ chọn **Build and deploy from a Git repository**.
4. Màn hình sẽ hiển thị danh sách kho lưu trữ GitHub của bạn. Bấm **Connect** bên cạnh tên `ktx-baohong-app`.

---

## Bước 3: Cấu hình Server (Rất Quan Trọng!!!)
Giao diện cài đặt hiện ra, bạn điền chính xác như sau:
* **Name**: `he-thong-ktx-baohong` (hay gì cũng được, nó sẽ trở thành tên miền truy cập của bạn: *he-thong-ktx-baohong.onrender.com*).
* **Region**: *Singapore* (hoặc US/EU mặc định).
* **Branch**: `main`.
* **Environment**: `Python 3`.
* **Build Command**: Nhập `pip install -r requirements.txt`. Lệnh này cài các thư viện Flask bạn cần.
* **Start Command**: Nhập `gunicorn app:app`. (Đây là phần mềm chạy server siêu mạnh, tôi đã gài sẵn vào requirements.txt cho bạn).
* **Instance Type**: Chọn gói **Free ($0/month)**.

🔴 **BƯỚC BẢO MẬT CỰC KỲ QUAN TRỌNG**:
Kéo xuống dưới cùng tìm chữ **Advanced**, bấm vào để mở rộng:
1. Nhấn nút **Add Environment Variable**.
2. Ô **Key** bạn gõ chính xác: `DB_PASSWORD`
3. Ô **Value** bạn copy đoạn mã này dán vào: `AVNS_-fw1clryaH3lS2yA1S1`

6. (Tùy chọn nhưng rất quan trọng) Thêm 3 biến môi trường cho việc **Lưu trữ ảnh Cloudinary** (Vì web miễn phí online thường tự xóa ảnh sau vài phút):
   * Nhấn nút **Add Environment Variable** thêm 3 lần nữa và nhập:
     * `CLOUDINARY_CLOUD_NAME` = Tên Cloud của bạn
     * `CLOUDINARY_API_KEY` = API Key của bạn
     * `CLOUDINARY_API_SECRET` = API Secret của bạn
   *(Để có 3 thông số này, bạn truy cập [Cloudinary.com](https://cloudinary.com/), bấm Sign Up for Free để đăng ký bằng Google. Sau khi đăng nhập, tại trang chủ Dashboard bạn sẽ lấy đoạn code chứa 3 thông tin này ở mục **Product Environment Credentials**).*

Cuối cùng, kéo xuống và nhấn nút xanh **Create Web Service**.

---

## Bước 4: Tận hưởng kết quả
* Render sẽ tự động chạy lệnh tải mã nguồn, cài thư viện và khởi động Web Server. Bạn đợi khoảng **2 đến 3 phút** cho đến khi trên màn hình Console hiện chữ: `Your service is live 🎉`.
* Ở trên cùng bên trái màn hình sẽ có một đường link màu xanh rêu (ví dụ: `https://he-thong-ktx-baohong.onrender.com`).
* **Hãy nhấn vào đường link đó!** Và BÙM, Website báo hỏng KTX của bạn đã chính thức nằm trên môi trường Internet. Bạn có thể gửi link này cho Kỹ thuật viên, Sinh viên, Quản lý để xài ngay trên Điện thoại và Máy tính của họ!!!

### Lợi Thế Sau Này:
Vì mã nguồn kết nối GitHub, sau này ở máy tính `d:\TTCN_BaoHongKTX` bạn code thêm API mới hay sửa HTML, bạn chỉ cần gõ:
```bash
git add .
git commit -m "Sua HTML"
git push
```
Lập tức trang web Online Render tự động tải bản code mới về và Restart Server. Bạn không phải thao tác tay thêm lần nào nữa! Chúc bạn thành công.
