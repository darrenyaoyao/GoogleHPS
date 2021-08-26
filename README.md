# Google Hardware Product Sprint－2021 APAC TW HPS
- **Project name**：Demeter
- **Mentor**：Weihsuan
- **Team**：2

## Wiring to Raspberry Pi

- [**［I2C］Air Quality**：SGP30](https://github.com/darrenyaoyao/GoogleHPS/tree/main/AirQuality#raspberry-pi-and-sgp30-wired-with-i2c)
- **［SPI］G-Sensor**：ADXL203EB
- **［I2C］Light**：APDS9960
- **［I2C］Temperature & Humidity**：SHT31-D

### Check the I2C devices

- **Air Quality**：`0x58`
- **Light**：`0x39`
- **Temperature & Humidity**：`0x44`

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

## Install Libraries

```
sudo pip3 install -r requirements.txt
```

## Run Web Server

```
sudo python3 SmartGardener.py
```

## Open the Website：http://[your ip]

- use `ifconfig` to check your ip
- replace `[your ip]` to something like `192.xxx.x.xx` or `192.xxx.x.xxx`

### Screenshot with Day theme and Nithgt theme（Automatic switching）

<img src="https://github.com/darrenyaoyao/GoogleHPS/blob/main/Photos/web.png" width='100%' height='100%'/>

### Buzzier

Connect ground to Buzzier negative pin, Raspberry Pi pin 16 (GPIO 23) to Buzzier positive pin

### Relay and Pump

Relay's VCC connect pin4(5v5)

Relay's GND connect pin6(GND)

Relay's IN connect pin18(GPIO24)



Relay's NO connect pin17(3v3)

Relay's COM connect Pump's red wire

Pump's black wire connect ground
