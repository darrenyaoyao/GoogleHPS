# Google Hardware Product Sprint－2021 APAC TW HPS

- **Project name**：Smart Gardener  

# Wiring to Raspberry Pi

- [**Air Quality**：SGP30](https://github.com/darrenyaoyao/GoogleHPS/tree/main/AirQuality#raspberry-pi-and-sgp30-wired-with-i2c)
- **G-Sensor**：ADXL203EB
- **Light**：APDS9960
- **Temperature & Humidity**：SHT31-D

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
