import datetime

class timeInfo:
    def __init__(self):
        self.waterYear = ' '
        self.waterMonth = ' '
        self.waterDay = ' '
        self.waterHour = ' '
        self.waterMinute = ' '
        self.noiseYear = ' '
        self.noiseMonth = ' '
        self.noiseDay = ' '
        self.noiseHour = ' '
        self.noiseMinute = ' '
        
        return
    
    def update_last_watering_year(self,year):
        self.waterYear = year
        
    def update_last_watering_month(self,month):
        self.waterMonth = month
    
    def update_last_watering_day(self,day):
        self.waterDay = day
    
    def update_last_watering_hour(self,hour):
        self.waterHour = hour
    
    def update_last_watering_minute(self,minute):
        self.waterMinute = minute
    
    def get_last_watering_time(self):
        return self.waterMonth + '月' + self.waterDay + '日 ' + self.waterHour + ':' + self.waterMinute
    
    def update_last_noise_year(self,year):
        self.noiseYear = year
        
    def update_last_noise_month(self,month):
        self.noiseMonth = month
    
    def update_last_noise_day(self,day):
        self.noiseDay = day
    
    def update_last_noise_hour(self,hour):
        self.noiseHour = hour
    
    def update_last_noise_minute(self,minute):
        self.noiseMinute = minute
    
    def get_last_noise_time(self):
        return self.noiseMonth + '月' + self.noiseDay + '日 ' + self.noiseHour + ':' + self.noiseMinute
