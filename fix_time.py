import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
conn = mysql.connector.connect(
    host=os.environ.get('DB_HOST', 'mysql-ktxbaohong-ktxbaohong-2026.e.aivencloud.com'),
    port=int(os.environ.get('DB_PORT', 28894)),
    user=os.environ.get('DB_USER', 'avnadmin'),
    password=os.environ.get('DB_PASSWORD', ''),
    database=os.environ.get('DB_NAME', 'defaultdb'),
    charset='utf8mb4',
    ssl_disabled=False
)
cur = conn.cursor()
try:
    print("Fixing phieubaohong DATETIME...")
    cur.execute("UPDATE phieubaohong SET ngay_tao = DATE_ADD(ngay_tao, INTERVAL 7 HOUR)")
    conn.commit()
    print("Fixing nguoidung DATETIME...")
    cur.execute("UPDATE nguoidung SET ngay_tao = DATE_ADD(ngay_tao, INTERVAL 7 HOUR)")
    conn.commit()
    print("Done!")
except Exception as e:
    print("Error:", e)
finally:
    cur.close()
    conn.close()
