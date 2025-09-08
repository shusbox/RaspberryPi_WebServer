import pymysql

# 1. 연결
conn = pymysql.connect(host='localhost', user='suhwa', password='q1w2e3', db='shopping_db2')

# 2. 커서
cur = conn.cursor()

# 3. 쿼리작성
cur.execute("select avg(age) from CUSTOMER where address = '경기'")

# 4. 결과값 조회
result = cur.fetchone()
# for r in result:
    # for j in r:
        # if j == '홍길동':
            # print(j)
print(round(result[0], 0))

# 5. 종료 (연결해제)
cur.close()
conn.close()
