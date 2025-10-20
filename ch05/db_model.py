import pymysql

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'q1w2e3'
DB_NAME = 'servo_db'

def add_angle(angle):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    try:
        cur = conn.cursor()
        # 안전하게 파라미터 처리
        cur.execute("INSERT INTO record_angle (angle) VALUES (%s)", (angle,))
        conn.commit()
    finally:
        conn.close()
