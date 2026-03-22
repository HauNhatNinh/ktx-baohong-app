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
cur = conn.cursor(dictionary=True)
cur.execute("SELECT tai_khoan, ngay_tao FROM nguoidung ORDER BY ngay_tao DESC LIMIT 1")
for row in cur.fetchall():
    print("nguoidung:", row)
    
cur.close()
conn.close()
