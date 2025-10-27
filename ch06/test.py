import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT11(board.D14, use_pulseio=False)

while True:
    try:
        temp = sensor.temperature
        hum = sensor.humidity
        print([temp, hum])
    except RuntimeError as e:
        print(f"Read failed: {e}. Retrying...")
    time.sleep(2)
