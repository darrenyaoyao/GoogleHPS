# For temperature and humidity (SHT31-D) 

## First 

### Pin

Connect VIN(1), GND(6), SCL(5), SDA(3) to raspberry pi. 

### Configuration 

Open raspberry pi configuration. 

```
sudo raspi-config
```

Check whether the configuration of I2C is enabled. 

    raspi-config \ interfacing \ options \ I2C Enabled 

## Second 

### Install I2C 

Install I2C tools. 

```
sudo apt install i2c-tools
```

### Detect I2C 

Detect whether I2C is worked. 

SHT31-D for raspberry pi has the address 0x44. 

```
i2cdetect -y 1
```

## Third 

### Install SHT31-D 

Install the library for SHT31-D. 

```
sudo pip3 install adafruit-circuitpython-sht31d
```

## Reference 

[1] SHT31 Temperature/Humidity Sensor and Rasperry Pi Zero W - Test and Review (#127)

https://www.youtube.com/watch?v=_f0ZZ7d_RdU&ab_channel=MartynDavies 

[2] Adafruit SHT31-D Temperature & Humidity Sensor Breakout

https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout/python-circuitpython 
