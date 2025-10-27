import time
import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D14)  # 기존과 동일

def get_now():
    for _ in range(3):  # 최대 3회 재시도
        try:
            temp = sensor.temperature
            hum = sensor.humidity
            return temp, hum
        except RuntimeError:
            time.sleep(1.5)  # 센서 안정화 시간
    return None, None  # 그래도 안되면 실패 처리
