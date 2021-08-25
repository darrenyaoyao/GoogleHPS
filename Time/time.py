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
        self.waterYear = year
        
    def update_last_watering_month(month):
        self.waterMonth = month
    
    def update_last_watering_day(day):
        self.waterDay = day
    
    def update_last_watering_hour(hour):
        self.waterHour = hour
    
    def update_last_watering_minute(minute):
        self.waterMinute = minute
    
    def get_last_watering_time(self):
        return self.waterMonth + '月' + self.waterDay + '日 ' + self.waterHour + ':' + self.waterMinute
    
    def update_last_noise_year(year):
        self.noiseYear = year
        
    def update_last_noise_month(month):
        self.noiseMonth = month
    
    def update_last_noise_day(day):
        self.noiseDay = day
    
    def update_last_noise_hour(hour):
        self.noiseHour = hour
    
    def update_last_noise_minute(minute):
        self.noiseMinute = minute
    
    def get_last_noise_time(self):
        return self.noiseMonth + '月' + self.noiseDay + '日 ' + self.noiseHour + ':' + self.noiseMinute
