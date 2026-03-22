import mysql.connector
from dotenv import load_dotenv
import os

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
cursor = conn.cursor(dictionary=True)
cursor.execute('SELECT anh_minh_chung FROM phieubaohong ORDER BY ma_phieu DESC LIMIT 5')
for row in cursor.fetchall():
    print(f"File: '{row.get('anh_minh_chung')}'")
conn.close()
