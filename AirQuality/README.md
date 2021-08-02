# [Air quality sensor：SGP30 TVOC/eCO2 Gas Sensor](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sgp30-gas-tvoc-eco2-mox-sensor.pdf)
## 簡介
- 使用 I2C 介面
- 適合室內使用
- 可檢測 VOC（揮發性有機化合物）和 H₂
- 沒有 eCO₂ sensor，但會用 H₂ 濃度推算出來
## Power Pins
- VIN：電源接角
- 1V8：可穩定輸出 1.8V，但應該用不到
- GND：接地
## Data Pins
- SCL：I2C clock 接角
- SDA：I2C data 接角
# Raspberry Pi 和 SGP30 接線（wired with I2C）
|SGP30|Raspberry Pi|
|:-:|:-:|
|VIN|3V3|
|GND|GND|
|SCL|SCL|
|SDA|SDA|

沒用到 1V8 Pin
## Raspberry Pi GPIO
3V3：1、17 號  
GND：6、9、14、20、25、30、34、39 號  
SCL：5 號  
SDA：3 號
## 檢查是否接對
接好線可以在 Terminal 中用：  

    sudo i2cdetect -y 1  
檢查有沒有接對！  
有的話，會看到：I2C adress 0x58  
# 下載：[CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
在 Terminal 中：

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade setuptools
    cd ~
    sudo pip3 install --upgrade adafruit-python-shell
    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    sudo python3 raspi-blinka.py
可能會問「Continue？」輸入 y，Enter
# 下載：[Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)
在 Terminal 中：

    pip3 install adafruit-circuitpython-lis3dh
# 下載：[adafruit_sgp30.mpy](https://github.com/adafruit/Adafruit_CircuitPython_SGP30)
在 Terminal 中：

    pip3 install adafruit-circuitpython-sgp30
# 下載：[adafruit_bus_device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/tree/5aceeae814effae4eb950f1078c194b11401faa7)
在 Terminal 中：

    pip3 install adafruit-circuitpython-busdevice
# 下載注意
如果有問題，可以改試試看  

    pip
不要  

    pip3
