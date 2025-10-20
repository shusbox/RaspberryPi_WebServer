@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        try:
            setAngle(int(angle))
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