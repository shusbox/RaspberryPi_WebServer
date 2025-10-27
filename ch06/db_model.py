import pymysql
import pymysql.cursors
from datetime import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'q1w2e3'
DB_NAME = 'dht_db'

def add_dht(dht):
    conn = pymysql.connect(
        host=DB_HOST, 
        user=DB_USER, 
        password=DB_PASS, 
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO dht11_data (temperature, humidity, create_at)
                VALUES (%s, %s, %s)
            """
            now = datetime.now()
            cursor.execute(sql, (dht['temperature'], dht['humidity'], now))
        conn.commit()
    finally:
        conn.close()

# Flask에서 편하게 호출할 수 있도록 alias 함수 추가
def add(temp, hum):
    add_dht({'temperature': temp, 'humidity': hum})

def find_all():
    conn = pymysql.connect(
        host=DB_HOST, 
        user=DB_USER, 
        password=DB_PASS, 
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM dht11_data ORDER BY create_at DESC"
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows
    finally:
        conn.close()