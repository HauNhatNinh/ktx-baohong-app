import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def tao_cot_moi():
    print("Connecting to DB to add columns email and anh_the_sv...")
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
        cursor = conn.cursor()
        
        try:
            cursor.execute("ALTER TABLE nguoidung ADD COLUMN email VARCHAR(255)")
            print("Added email column")
        except Exception as e:
            print(f"email column might already exist: {e}")
            
        try:
            cursor.execute("ALTER TABLE nguoidung ADD COLUMN anh_the_sv VARCHAR(255)")
            print("Added anh_the_sv column")
        except Exception as e:
            print(f"anh_the_sv column might already exist: {e}")
            
        conn.commit()
        print("DONE! DB updated.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    tao_cot_moi()
