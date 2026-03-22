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
            charset='utf8mb4'
        )
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT tai_khoan, email FROM nguoidung WHERE vai_tro='sinhvien'")
for row in cursor.fetchall():
    print(row)
conn.close()
