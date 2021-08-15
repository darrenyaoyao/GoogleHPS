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

    def cold_or_hot(self):
        TData = sensorSHT31.temperature
        if TData > 27 : return "It's very hot！！"
        elif TData > 23 : return "It's hot！"
        elif TData > 21 : return "It's warm."
        elif TData > 17 : return "It's comfortable."
        elif TData > 9 : return "It's cool."
        elif TData > 1 : return "It's cold！"
        else : return "It's very cold！！"
    
    def dry_or_wet(self):
        RHData = sensorSHT31.relative_humidity
        if RHData > 80 : return "The humidity is high！"
        elif RHData > 60 and RHData < 80 : return "It's comfortable."
        else : return "It's dry！"
