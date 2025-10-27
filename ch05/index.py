from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep
import db_model
import threading

app = Flask(__name__)

# ---------------------
# 서보 설정
# ---------------------
PIN = 16  # BOARD 기준 핀 번호
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)  # 50Hz
servo.start(0)

running = False

def rotate_continuous():
    global running
    while running:
        # 0도 -> 180도 -> 0도 반복
        for angle in range(0, 181, 10):
            if not running:
                break
            duty = 2.5 + 10 * angle / 180
            servo.ChangeDutyCycle(duty)
            sleep(0.05)
        for angle in range(180, -1, -10):
            if not running:
                break
            duty = 2.5 + 10 * angle / 180
            servo.ChangeDutyCycle(duty)
            sleep(0.05)
    servo.ChangeDutyCycle(0) 


def setAngle(angle):
    global running
    if running:
        running = False
        sleep(0.1)
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

@app.route('/api/turn')
def start_rotation():
    global running
    if not running:
        running = True
        t = threading.Thread(target=rotate_continuous)
        t.start()
    return jsonify({'message': 'Rotation started'})

@app.route('/api/stop')
def stop_rotation():
    global running
    running = False
    return jsonify({'message': 'Rotation stopped'})

# ---------------------
# 서버 실행
# ---------------------
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        servo.stop()
        GPIO.cleanup()
