import datetime

class timeInfo:
    def __init__(self):
        self.waterYear = 0
        self.waterMonth = 0
        self.waterDay = 0
        self.waterHour = 0
        self.waterMinute = 0
        self.noiseYear = 0
        self.noiseMonth = 0
        self.noiseDay = 0
        self.noiseHour = 0
        self.noiseMinute = 0
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
    
    def get_last_watering_hour(self):
        return self.waterHour
    
    def get_last_watering_minute(self):
        return self.waterMinute
    
    def get_last_watering_time(self):
        return str(self.waterMonth) + '月' + str(self.waterDay) + '日 ' + str(self.waterHour).zfill(2) + ':' + str(self.waterMinute).zfill(2)
    
    def upon_last_watering_time(self):
        minute = self.waterHour * 60 + self.waterMinute - datetime.datetime.now().hour *60 - datetime.datetime.now().minute
        return str(minute) + '分'
    
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
    
    def get_last_noise_hour(self):
        return self.noiseHour
    
    def get_last_noise_minute(self):
        return self.noiseMinute
    
    def get_last_noise_time(self):
        return str(self.noiseMonth) + '月' + str(self.noiseDay) + '日 ' + str(self.noiseHour).zfill(2) + ':' + str(self.noiseMinute).zfill(2)

    def upon_last_noise_time(self):
        minute = self.noiseHour * 60 + self.noiseMinute - datetime.datetime.now().hour *60 - datetime.datetime.now().minute
        return str(minute) + '分'
