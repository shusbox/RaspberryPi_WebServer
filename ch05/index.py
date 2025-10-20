from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep
import db_model

app = Flask(__name__)

# ---------------------
# 서보 설정
# ---------------------
PIN = 16  # BOARD 기준 핀 번호
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)  # 50Hz
servo.start(0)

def setAngle(angle):
    duty = 2.5 + 10 * angle / 180
    print(f"Setting angle: {angle} -> Duty: {duty}")
    servo.ChangeDutyCycle(duty)
    sleep(0.5)  # 서보 이동 시간
# ---------------------
# 라우트
# ---------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        try:
            setAngle(int(angle))
            db_model.add_angle(int(angle))
            return jsonify({'message': f'Angle set to {angle}'})
        except Exception as e:
            return jsonify({'message': f'Error: {str(e)}'})
    else:
        return jsonify({'message': 'Fail! Check your parameter'})

# ---------------------
# 서버 실행
# ---------------------
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        servo.stop()
        GPIO.cleanup()
