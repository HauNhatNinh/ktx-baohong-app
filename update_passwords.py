import mysql.connector
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash

load_dotenv()

def cap_nhat_mat_khau():
    print("Connecting to Database...")
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'mysql-ktxbaohong-ktxbaohong-2026.e.aivencloud.com'),
            port=int(os.environ.get('DB_PORT', 28894)),
            user=os.environ.get('DB_USER', 'avnadmin'),
            password=os.environ.get('DB_PASSWORD', ''),
            database=os.environ.get('DB_NAME', 'defaultdb'),
            charset='utf8mb4',
            ssl_disabled=False
        )
        cursor = conn.cursor(dictionary=True)
        
        # Ở đây dùng lệnh lấy ma_nguoidung:
        cursor.execute("SELECT ma_nguoidung, tai_khoan, mat_khau FROM nguoidung")
        nguoi_dungs = cursor.fetchall()
        
        so_luong_da_cap_nhat = 0
        
        for nd in nguoi_dungs:
            mk_hien_tai = nd['mat_khau']
            
            # Kiểm tra xem mật khẩu đã được mã hoá (bắt đầu bằng 'scrypt:' hoặc 'pbkdf2:') hay chưa
            if not mk_hien_tai.startswith('scrypt:') and not mk_hien_tai.startswith('pbkdf2:'):
                mk_moi_da_ma_hoa = generate_password_hash(mk_hien_tai)
                
                # Cập nhật lại mật khẩu trong DB
                update_cursor = conn.cursor()
                update_cursor.execute(
                    "UPDATE nguoidung SET mat_khau = %s WHERE ma_nguoidung = %s",
                    (mk_moi_da_ma_hoa, nd['ma_nguoidung'])
                )
                conn.commit()
                so_luong_da_cap_nhat += 1
                update_cursor.close()
                print(f"Updated password for: {nd['tai_khoan']}")
        
        print(f"\nDONE! Updated {so_luong_da_cap_nhat} accounts in Database.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    cap_nhat_mat_khau()
