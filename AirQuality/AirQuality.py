import time
import math
import board
import busio
import adafruit_sgp30
import adafruit_sht31d

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
sht31d = adafruit_sht31d.SHT31D(i2c)

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

RH = int(sht31d.relative_humidity)
t = int(sht31d.temperature)
AH = 216.7 * ((RH / 100.0) * 6.112 * math.exp((17.62 * t) / (243.12 + t)) / (273.15 + t))
sgp30.set_iaq_humidity(AH)

class AirQuality:
    def __init__(self):
        return
    
    def get_eCO2_Data(self):
        return sgp30.eCO2
    
    def get_TVOC_Data(self):
        return sgp30.TVOC
    
    def get_Ethanol_Data(self):
        return sgp30.Ethanol # maybe ppb
    
    def get_H2_Data(self):
        return sgp30.H2 # maybe ppb

    def good_or_bad(self):
        # CO₂ standard：average 1000 ppm within 8 hours
        # TVOC standard：average 0.56 ppm within 1 hours
        if sgp30.eCO2 <= 1000 and sgp30.TVOC*1000 <= 0.56 :
            return "Air quality can't be better！"
        elif sgp30.eCO2 > 1000 and sgp30.TVOC*1000 <= 0.56 :
            return 'It seems that CO₂ is too high！'
        elif sgp30.eCO2 <= 1000 and sgp30.TVOC*1000 > 0.56 :
            return 'It seems that TVOC is too high！'
        else : return 'Both CO₂ and TVOC are too high！Bad air quality！Very bad......'
