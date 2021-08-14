import math
import board
import busio
import adafruit_sgp30
import adafruit_sht31d

class AirQuality:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        self.sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
        self.sht31d = adafruit_sht31d.SHT31D(i2c)
        
        self.sgp30.iaq_init()
        self.sgp30.set_iaq_baseline(0x8973, 0x8AAE)
        
        RH = int(self.sht31d.relative_humidity)
        t = int(self.sht31d.temperature)
        AH = 216.7 * ((RH / 100.0) * 6.112 * math.exp((17.62 * t) / (243.12 + t)) / (273.15 + t))
        self.sgp30.set_iaq_humidity(AH)
        
        self.last_read_eCO2 = 0
        self.last_read_eCO2_time = 0
        self.last_read_TVOC = 0
        self.last_read_TVOC_time = 0
        
        return
    
    def get_eCO2_Data(self):
        self.last_read_eCO2 += self.sgp30.eCO2
        self.last_read_eCO2_time += 1
        return self.sgp30.eCO2
    
    def get_TVOC_Data(self):
        self.last_read_TVOC += self.sgp30.TVOC
        self.last_read_TVOC_time += 1
        return self.sgp30.TVOC
    
    def get_Ethanol_Data(self):
        return self.sgp30.Ethanol # maybe ppb
    
    def get_H2_Data(self):
        return self.sgp30.H2 # maybe ppb

    def good_or_bad(self):
        # CO₂ standard：average 1000 ppm within 8 hours
        # TVOC standard：average 0.56 ppm within 1 hours
        self.last_read_eCO2 += self.sgp30.eCO2
        self.last_read_eCO2_time += 1
        self.last_read_TVOC += self.sgp30.TVOC
        self.last_read_TVOC_time += 1
        
        if self.last_read_eCO2/self.last_read_eCO2_time <= 1000 and (self.last_read_TVOC/self.last_read_TVOC_time)*1000 <= 0.56 :
            return "Can't be better！"
        elif self.last_read_eCO2/self.last_read_eCO2_time > 1000 and (self.last_read_TVOC/self.last_read_TVOC_time)*1000 <= 0.56 :
            return 'It seems that CO₂ is too high！'
        elif self.last_read_eCO2/self.last_read_eCO2_time <= 1000 and (self.last_read_TVOC/self.last_read_TVOC_time)*1000 > 0.56 :
            return 'It seems that TVOC is too high！'
        else : return 'Both CO₂ and TVOC are too high！So bad......'
