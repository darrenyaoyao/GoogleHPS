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
    
    def getTemperatureF(self):
        #print('Temp = {:.1f} \u00b0C'.format(sensorSHT31.temperature))
        TFData = format(sensorSHT31.temperature * 9 / 5 + 32, '.3f')
        return TFData

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
        TData = sensorSHT31.temperature
        if RHData > 80 : return "It's humid for plants！"
        elif RHData > 60 and RHData < 80 and TData > 22 and TData < 32 : return "Plants feel comfortable～"
        elif RHData > 60 and RHData < 80 : return "It's good for plants."
        else : return "It's dry for plants！"
        
    def dry_or_wet_people(self):
        RHData = sensorSHT31.relative_humidity
        TData = sensorSHT31.temperature
        if RHData > 65 : return "It's humid for people！"
        elif RHData > 45 and RHData < 65 and TData > 18 and TData < 23 : return "People feel comfortable～"
        elif RHData > 45 and RHData < 65 : return "It's good for people."
        else : return "It's dry for people！"

    def auto_water(self):
        RHData = sensorSHT31.relative_humidity
        TData = sensorSHT31.temperature
        if RHData < 60 : return true
        else : return false
