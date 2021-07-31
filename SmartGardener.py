from flask import Flask
from AirQuality.AirQuality import AirQuality
from GSensor.GSensor import GSensor
from Light.Light import Light
from TemperatureHumidity.TemperatureHumidity import TemperatureHumidity

app = Flask("Smart Gardener")
airQuality = AirQuality()
gsensor = GSensor()
light = Light()
temperatureHumidity = TemperatureHumidity()


@app.route("/")
def home():
    return "空氣品質: " + str(airQuality.getData()) + "<br/>" + \
           "GSensor: " + str(gsensor.getData()) + "<br/>" + \
           "陽光強度: " + str(light.getData()) + "<br/>" + \
           "溫度: " + str(temperatureHumidity.getTemperatureData()) + "<br/>" + \
           "濕度: " + str(temperatureHumidity.getHumidityData())
