# APDS9960
## I2C Wiring
![GITHUB](https://cdn-learn.adafruit.com/assets/assets/000/058/685/original/light_raspi_apds9960_i2c_bb.png?1533613053)
## Detect I2C
`sudo i2cdetect -y 1`

    pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

## Installing from PyPI
`pip3 install adafruit-circuitpython-apds9960`
## Usage Example
```python
    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT

          import time
          import board
          from adafruit_apds9960.apds9960 import APDS9960
          from adafruit_apds9960 import colorutility

          i2c = board.I2C()
          apds = APDS9960(i2c)
          apds.enable_color = True


          while True:
               # create some variables to store the color data in

               # wait for color data to be ready
               while not apds.color_data_ready:
                    time.sleep(0.005)
                    
                    
          print("color temp {}".format(colorutility.calculate_color_temperature(r, g, b)))
          print("light lux {}".format(colorutility.calculate_lux(r, g, b)))
          time.sleep(0.5)
                    
```
          
