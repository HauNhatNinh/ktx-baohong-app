import mysql.connector
import os
from dotenv import load_dotenv
import json

load_dotenv()
conn = mysql.connector.connect(
    host=os.environ.get('DB_HOST', 'mysql-ktxbaohong-ktxbaohong-2026.e.aivencloud.com'),
    port=int(os.environ.get('DB_PORT', 28894)),
    user=os.environ.get('DB_USER', 'avnadmin'),
    password=os.environ.get('DB_PASSWORD', ''),
    database=os.environ.get('DB_NAME', 'defaultdb'),
    charset='utf8mb4'
)
cur = conn.cursor(dictionary=True)
cur.execute("SHOW TABLES")
tables = [list(t.values())[0] for t in cur.fetchall()]

schema = {}
for tbl in tables:
    cur.execute(f"SHOW COLUMNS FROM {tbl}")
    cols = cur.fetchall()
    schema[tbl] = cols

print(json.dumps(schema, indent=2))
cur.close()
conn.close()
