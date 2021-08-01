import board
import busio
import adafruit_sht31d
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensorSHT31 = adafruit_sht31d.SHT31D(i2c, 0x44)

class TemperatureHumidity:
    def __init__(self):
        return

    def getTemperatureData(self):
        print('Temp = {:.1f} \u00b0C'.format(sensorSHT31.temperature))
        return

    def getHumidityData(self):
        print('RH = {:.1f} %\n'.format(sensorSHT31.relative_humidity))
        return 50
