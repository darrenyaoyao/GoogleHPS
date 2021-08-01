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
        return 100
    
    def get_eCO2_Data(self):
        return sgp30.eCO2 # ppm
    
    def get_TVOC_Data(self):
        return sgp30.TVOC # ppb
