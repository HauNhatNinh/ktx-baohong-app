import re

file_path = "d:\\TTCN_BaoHongKTX\\app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "'Loi ket noi database'": "'Lỗi kết nối cơ sở dữ liệu'",
    "'Sai tai khoan hoac mat khau'": "'Sai tài khoản hoặc mật khẩu'",
    "'Tai khoan dang cho duyet. Vui long lien he quan ly KTX.'": "'Tài khoản đang chờ duyệt. Vui lòng liên hệ quản lý ký túc xá.'",
    "'Yeu cau dang ky da bi tu choi.'": "'Yêu cầu đăng ký đã bị từ chối.'",
    "'Dang nhap thanh cong'": "'Đăng nhập thành công'",
    "'Vui long dien day du thong tin'": "'Vui lòng điền đầy đủ thông tin'",
    "'Ma so sinh vien da duoc dang ky'": "'Mã số sinh viên đã được đăng ký'",
    "'Dang ky thanh cong! Vui long cho quan ly KTX duyet tai khoan.'": "'Đăng ký thành công! Vui lòng chờ quản lý KTX duyệt tài khoản.'",
    "'Chua dang nhap'": "'Chưa đăng nhập'",
    "'Cap nhat thanh cong'": "'Cập nhật thành công'",
    "'Vui long nhap ten loi hong'": "'Vui lòng nhập tên lỗi hỏng'",
    "'Khong tim thay thong tin phong'": "'Không tìm thấy thông tin phòng'",
    "'Tao phieu bao hong thanh cong!'": "'Tạo phiếu báo hỏng thành công!'",
    "'Phan cong thanh cong'": "'Phân công thành công'",
    "'Da huy phieu bao hong'": "'Đã huỷ phiếu báo hỏng'",
    "'Da xac nhan hoan thanh'": "'Đã xác nhận hoàn thành'",
    "'Da tu choi xac nhan. Yeu cau ky thuat vien sua lai.'": "'Đã từ chối xác nhận. Yêu cầu kỹ thuật viên sửa lại.'",
    "f'Da {\"duyet\" if chap_nhan else \"tu choi\"} tai khoan'": "f'Đã {\"duyệt\" if chap_nhan else \"từ chối\"} tài khoản'",
    "'Cap nhat thong tin thanh cong'": "'Cập nhật thông tin thành công'",
    "'Da tiep nhan phieu sua chua'": "'Đã tiếp nhận phiếu sửa chữa'",
    "'Da tu choi. Phieu da bi huy.'": "'Đã từ chối. Phiếu đã bị huỷ.'",
    "'Da gui minh chung hoan thanh'": "'Đã gửi minh chứng hoàn thành'",
    "'Vai tro khong hop le'": "'Vai trò không hợp lệ'",
    "'Tai khoan da ton tai'": "'Tài khoản đã tồn tại'",
    "f'Tao tai khoan {vai_tro} thanh cong'": "f'Tạo tài khoản {vai_tro} thành công'",
    "'Da xoa tai khoan'": "'Đã xoá tài khoản'"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done translations in app.py")
