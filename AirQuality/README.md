# [Air quality sensor：SGP30 TVOC/eCO2 Gas Sensor](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sgp30-gas-tvoc-eco2-mox-sensor.pdf)
<img src="https://github.com/darrenyaoyao/GoogleHPS/blob/main/AirQuality/Photos/SGP30.png" width='30%' height='30%'/>

> ## 簡介
- 使用 I2C 介面
- 適合室內使用
- 可檢測 VOC（揮發性有機化合物）和 H₂
- 沒有 eCO₂ sensor，但會用 H₂ 濃度推算出來（IAQ 演算法）
> ## Power Pins
- **VIN**：電源接角
- **1V8**：可穩定輸出 1.8V，但應該用不到
- **GND**：接地
> ## Data Pins
- **SCL**：I2C clock 接角
- **SDA**：I2C data 接角
# Raspberry Pi 和 SGP30 接線（wired with I2C）
<img src="https://github.com/darrenyaoyao/GoogleHPS/blob/main/AirQuality/Photos/Raspberry%20Pi%20%26%20SGP30%20wired%20with%20I2C.png" width='60%' height='60%'/>

|SGP30|Raspberry Pi|
|:-:|:-:|
|VIN|3V3|
|GND|GND|
|SCL|SCL|
|SDA|SDA|

沒用到 1V8 Pin
> ## Raspberry Pi GPIO Pin
- **3V3**：1、17 號  
- **GND**：6、9、14、20、25、30、34、39 號  
- **SCL**：5 號  
- **SDA**：3 號
<img src="https://github.com/darrenyaoyao/GoogleHPS/blob/main/AirQuality/Photos/Raspberry%20Pi%20GPIO.png" width='95%' height='95%'/>

> ## 檢查是否接對
接好線可以在 Terminal 中用：`sudo i2cdetect -y 1`
檢查有沒有接對！  
有的話，會看到：I2C adress 0x58

    pi@raspberrypi:~ $ sudo i2cdetect -y 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --
# 下載 Library
> ## 在 Terminal 中下載 [CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade setuptools
    cd ~
    sudo pip3 install --upgrade adafruit-python-shell
    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    sudo python3 raspi-blinka.py
可能會問「Continue？」輸入 y，Enter
> ## 在 Terminal 中下載 [Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)

    pip3 install adafruit-circuitpython-lis3dh
> ## 在 Terminal 中下載 [adafruit_sgp30.mpy](https://github.com/adafruit/Adafruit_CircuitPython_SGP30)

    pip3 install adafruit-circuitpython-sgp30
> ## 在 Terminal 中下載 [adafruit_bus_device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/tree/5aceeae814effae4eb950f1078c194b11401faa7)

    pip3 install adafruit-circuitpython-busdevice
> ## 下載注意
如果有問題，可以改試試看 `pip` 不要 `pip3`
# [Using the SGP30 with CircuitPython and the Adafruit library](https://github.com/adafruit/Adafruit_CircuitPython_SGP30/blob/main/examples/sgp30_simpletest.py)
SGP30 簡單使用範例程式
```python
import time
import board
import busio
import adafruit_sgp30
    
# 定義 busio.I2C 和 sensor 物件
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

# IAQ 演算法：將 H₂ 濃度換算成 eCO₂ 的濃度
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0

while True:
    # 讀值：eCO₂ & TVOC
    print("eCO₂ = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))     
    time.sleep(1) # 等一下
    elapsed_sec += 1
    # 每 10 次輸出 1 次 Baseline values 和 IAQ 演算法有關
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO₂ = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
```
