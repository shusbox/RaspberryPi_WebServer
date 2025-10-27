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
        cursorclass=pymysql.cursors.DictCursor)
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