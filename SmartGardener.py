from flask import Flask, render_template, request
from AirQuality.AirQuality import AirQuality
from GSensor.GSensor import GSensor
from Light.Light import Light
from TemperatureHumidity.TemperatureHumidity import TemperatureHumidity

app = Flask("Smart Gardener")
airQuality = AirQuality()
gsensor = GSensor()
light = Light()
temperatureHumidity = TemperatureHumidity()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('Noise') == 'Noise':
            print('Noise')
        elif request.form.get('Water') == 'Water':
            print('Water')
    return render_template('home.html', airQuality_good_or_bad=airQuality.good_or_bad(),
            eCO2_Data=airQuality.get_eCO2_Data(),
            TVOC_Data=airQuality.get_TVOC_Data(),
            gsensor_data=str(gsensor.getData()),
            bright_ot_dark=light.bright_ot_dark(),
            light_value=light.getData(),
            coloe_lux=str(light.get_color_temperature_Data()),
            cold_or_hot=temperatureHumidity.cold_or_hot(),
            temperature=str(temperatureHumidity.getTemperatureData()),
            temperatureF=str(temperatureHumidity.getTemperatureF()),
            dry_or_wet=temperatureHumidity.dry_or_wet(),
            dry_or_wet_people=temperatureHumidity.dry_or_wet_people(),
            humidity=str(temperatureHumidity.getHumidityData()),)

if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
