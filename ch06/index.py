from flask import Flask, request, render_template, jsonify
import db_model
import sensor_dht
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/now')
def insertdb():
    # DHT 센서에서 현재 데이터 읽기
    temp, hum = sensor_dht.get_now()

    # DB에 삽입
    db_model.add(temp, hum)

    # 현재 시간 생성
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # JSON으로 응답
    return jsonify({
        "temperature": temp,
        "humidity": hum,
        "create_at": now
    })

@app.route('/api/record')
def selectAll():
    result = db_model.find_all()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")