import time
import board
import busio
import adafruit_sgp30

# 定義 busio.I2C 和 sensor 物件
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

# IAQ 演算法
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

class AirQuality:
    def __init__(self):
        return
    
    def getData(self):
        return str(sgp30.eCO2) + ' ppm ／ ' + str(sgp30.TVOC) + ' ppb'
    
    def get_eCO2_Data(self):
        return str(sgp30.eCO2) + ' ppm'
    
    def get_TVOC_Data(self):
        # 揮發性有機化合物
        return str(sgp30.TVOC) + ' ppb'
    
    def get_Ethanol_Data(self):
        # 乙醇濃度：不知道單位，但測都在 18000 上下
        return str(sgp30.Ethanol)
    
    def get_H2_Data(self):
        # H₂ 濃度：不知道單位，但測都在 13700 上下
        return str(sgp30.H2)

    def good_or_bad(self):
        # CO₂ 標準：8 小時內平均在 1000 ppm 以內
        # TVOC 標準：1 小時內平均在 0.56 ppm 以內
        if sgp30.eCO2 <= 1000 & sgp30.TVOC*1000 <= 0.56 :
            return 'Good air quality！'
        elif sgp30.eCO2 > 1000 & sgp30.TVOC*1000 <= 0.56 :
            return 'CO₂ is too high！'
        elif sgp30.eCO2 <= 1000 & sgp30.TVOC*1000 > 0.56 :
            return 'TVOC is too high！'
        else : return 'Both CO₂ and TVOC are too high！Bad air quality！'
