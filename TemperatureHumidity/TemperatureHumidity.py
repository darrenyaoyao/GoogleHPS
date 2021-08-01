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
        #print('Temp = {:.1f} \u00b0C'.format(sensorSHT31.temperature))
        TData = format(sensorSHT31.temperature, '.3f')
        return TData

    def getHumidityData(self):
        #print('RH = {:.1f} %\n'.format(sensorSHT31.relative_humidity))
        RHData = format(sensorSHT31.relative_humidity, '.3f')
        return RHData

RH = sensorSHT31.relative_humidity

class Watering:
    def __init__(self):
        return
    
    def getWateringData(self):
        if RH < 50.0:
            answer = "Need water. "
        elif RH > 60.0:
            answer = "Too much water. "
        else:
            answer = "It's fine now. "
        return answer
