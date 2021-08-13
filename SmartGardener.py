from flask import Flask
from AirQuality.AirQuality import AirQuality
from GSensor.GSensor import GSensor
from Light.Light import Light
from TemperatureHumidity.TemperatureHumidity import TemperatureHumidity
from TemperatureHumidity.TemperatureHumidity import Watering

app = Flask("Smart Gardener")
airQuality = AirQuality()
gsensor = GSensor()
light = Light()
temperatureHumidity = TemperatureHumidity()
watering = Watering()

@app.route("/")
def home():
    return "空氣品質：" + airQuality.good_or_bad() + "（eCO₂：" + str(airQuality.get_eCO2_Data()) + " ppm、TVOC：" + str(airQuality.get_TVOC_Data()) + " ppb）" + "<br/>" + \
           "G-Sensor：" + str(gsensor.getData()) + "<br/>" + \
           "陽光強度：" + str(light.getData()) + "<br/>" + \
           "溫度：" + str(temperatureHumidity.getTemperatureData()) + " °C<br/>" + \
           "濕度：" + str(temperatureHumidity.getHumidityData() + "％<br/r>" + \
           "澆水：" + str(watering.getWateringData()))

if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
