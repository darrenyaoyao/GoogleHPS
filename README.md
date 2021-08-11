# Google Hardware Product Sprint－2021 APAC TW HPS

- **Project name**：Smart Gardener  

# Wiring to Raspberry Pi

- [**Air Quality**：SGP30](https://github.com/darrenyaoyao/GoogleHPS/tree/main/AirQuality#raspberry-pi-and-sgp30-wired-with-i2c)
- **G-Sensor**：ADXL203EB
- **Light**：APDS9960
- **Temperature & Humidity**：SHT31-D

> ## Check the I2C devices

- **Air Quality**：0x58
- **Light**：0x39
- **Temperature & Humidity**：0x44

```
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

- **G-Sensor**：SPI interface

# Install Libraries

```
sudo pip3 install -r requirements.txt
```

# Run Web Server

```
sudo python3 SmartGardener.py
```

# Check your ip

```
ifconfig
```

open  
>http://[your ip]/

on your phone or laptop browser
