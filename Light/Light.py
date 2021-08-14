import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True

class Light:
    def __init__(self):
        return
    
    def getData(self):
        while not apds.color_data_ready:
            time.sleep(0.005)
        r,g,b,c = apds.color_data
        # a = colorutility.calculate_color_temperature(r, g, b)
        b = colorutility.calculate_lux(r, g, b)
        # ambient Max light values：34196.163
        return str(round(b,3)) + '（' + str(round(b / 34196.163,3)) + '％）'

    def get_color_temperature_Data(self):
        while not apds.color_data_ready:
            time.sleep(0.005)
        r,g,b,c = apds.color_data
        a = colorutility.calculate_color_temperature(r, g, b)
        return '色溫：' + str(round(a,3))
    
class Watering:
    def __init__(self):
        return
    
    def getWateringData(self):
        r,g,b,c = apds.color_data
        CL = colorutility.calculate_lux(r, g, b)  
        if RH > 2500:
            answer = "Need water. "
        else:
            answer = "It's fine now. "
        return answer
