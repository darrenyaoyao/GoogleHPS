import datetime

class timeInfo:
    def __init__(self):
        waterYear = ' '
        waterMonth = ' '
        waterDay = ' '
        waterHour = ' '
        waterMinute = ' '
        noiseYear = ' '
        noiseMonth = ' '
        noiseDay = ' '
        noiseHour = ' '
        noiseMinute = ' '
        
        return
    
    def update_last_watering_year(year):
        waterYear = year
        
    def update_last_watering_month(month):
        waterMonth = month
    
    def update_last_watering_day(day):
        waterDay = day
    
    def update_last_watering_hour(hour):
        waterHour = hour
    
    def update_last_watering_minute(minute):
        waterMinute = minute
    
    def get_last_watering_time(self):
        return self.waterMonth + '月' + self.waterDay + '日 ' + self.waterHour + ':' + self.waterMinute
    
    def update_last_noise_year(year):
        noiseYear = year
        
    def update_last_noise_month(month):
        noiseMonth = month
    
    def update_last_noise_day(day):
        noiseDay = day
    
    def update_last_noise_hour(hour):
        noiseHour = hour
    
    def update_last_noise_minute(minute):
        noiseMinute = minute
    
    def get_last_noise_time(self):
        return self.noiseMonth + '月' + self.noiseDay + '日 ' + self.noiseHour + ':' + self.noiseMinute
