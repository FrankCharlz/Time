__author__ = 'CharlesMagoti'
import  urllib

#url give curent time in Dar es Salaam '11-25-2015_16:00:46'
URL = 'http://www.timeapi.org/utc/in+three+hours?\m-\d-\Y_\H:\M:\S'

class Instant:
    def __init__(self):
        self.dt =  urllib.urlopen(URL).read()
        self.time = self.dt[-8:]
        self.date = self.dt[0:-9]

    def getTime(self):
        return self.time

    def getDate(self):
        return self.date
