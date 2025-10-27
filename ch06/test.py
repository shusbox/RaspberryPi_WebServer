import adafruit_dht
import board

sensor = adafruit_dht.DHT11(board.D14)

temp = sensor.temperature
hum = sensor.humidity
print([temp, hum])
