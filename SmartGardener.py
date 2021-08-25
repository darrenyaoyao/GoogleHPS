from flask import Flask, render_template, request
from AirQuality.AirQuality import AirQuality
from GSensor.GSensor import GSensor
from Light.Light import Light
from TemperatureHumidity.TemperatureHumidity import TemperatureHumidity
from Time.time import timeInfo
import RPi.GPIO as GPIO
import datetime
import time

app = Flask("Smart Gardener")
airQuality = AirQuality()
gsensor = GSensor()
light = Light()
temperatureHumidity = TemperatureHumidity()
timeInfo = timeInfo()

GPIO.setmode(GPIO.BCM)
BUZZIER=23
GPIO.setup(BUZZIER, GPIO.OUT)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('Noise') == 'Noise':
            print('Noise')
            timeInfo.update_last_noise_year(datetime.datetime.now().year)
            timeInfo.update_last_noise_month(datetime.datetime.now().month)
            timeInfo.update_last_noise_day(datetime.datetime.now().day)
            timeInfo.update_last_noise_hour(datetime.datetime.now().hour)
            timeInfo.update_last_noise_minute(datetime.datetime.now().minute)
            p = GPIO.PWM(BUZZIER, 50)
            p.start(50)
            p.ChangeFrequency(523)
            time.sleep(1)
            p.ChangeFrequency(587)
            time.sleep(1)
            p.ChangeFrequency(659)
            time.sleep(1)
            p.stop()
        elif request.form.get('Watering') == 'Watering':
               timeInfo.update_last_watering_year(str(datetime.datetime.now().year))
               timeInfo.update_last_watering_month(datetime.datetime.now().month)
               timeInfo.update_last_watering_day(datetime.datetime.now().day)
               timeInfo.update_last_watering_hour(datetime.datetime.now().hour)
               timeInfo.update_last_watering_minute(datetime.datetime.now().minute)
               print('Watering')
    return render_template('home.html',
                           airQuality_good_or_bad=airQuality.good_or_bad(),
                           eCO2_Data=airQuality.get_eCO2_Data(),
                           TVOC_Data=airQuality.get_TVOC_Data(),
                           gsensor_data=str(gsensor.getData()),
                           stable_or_sway=gsensor.stable_or_sway(),
                           bright_ot_dark=light.bright_ot_dark(),
                           light_value=light.getData(),
                           coloe_lux=str(light.get_color_temperature_Data()),
                           cold_or_hot=temperatureHumidity.cold_or_hot(),
                           temperature=str(temperatureHumidity.getTemperatureData()),
                           temperatureF=str(temperatureHumidity.getTemperatureF()),
                           dry_or_wet=temperatureHumidity.dry_or_wet(),
                           dry_or_wet_people=temperatureHumidity.dry_or_wet_people(),
                           humidity=str(temperatureHumidity.getHumidityData()),
                           year=datetime.datetime.now().year,
                           month=datetime.datetime.now().month,
                           day=datetime.datetime.now().day,
                           hour=datetime.datetime.now().hour,
                           minute=datetime.datetime.now().minute,
                           last_water_time=timeInfo.get_last_watering_time(),
                           last_noise_time=timeInfo.get_last_noise_time(),
                          )

if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
