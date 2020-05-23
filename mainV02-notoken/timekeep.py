"""
/ timeKeep.py
-----------------------------
/ author: paris osuch
/ website: parisosuch.com
/ git-hub repo: https://github.com/parisosuch-dev/
-----------------------------
/ about: utilizes datetime class from datetime module to create time data that is used
in the graphing and runtime process
-----------------------------
/ timeKeep() class
/ / systemTime() - method
/ / timeData() - method
/ / dayOfWeek() - method
/ / currentDate() - method
/ / newDay() - method
-----------------------------
"""
# / imports
from datetime import datetime

# / timeKeep Object
class TimeKeep:
    def __init__(self):
        self.second = datetime.now().second
        self.minute = datetime.now().minute
        self.hour = datetime.now().hour
        self.weekday = datetime.now().weekday()
        self.day = datetime.now().day
        self.month = datetime.now().month

    # / / system time method
    def systemTime(self):
        s = str(self.second)
        m = str(self.minute)
        h = str(self.hour)
        d = str(self.day)
        t = d+'d:'+h+'h:'+m+'m:'+s+'s' # Xd:Xh:Xm:Xs

        return t

    # / / time data method
    def timeData(self):
        time = [self.second, self.minute, self.hour, self.day] # [s, m, h, d]

        return time

    # / / day of the week method
    def dayOfWeek(self):
        day = self.weekday
        if day == 0:
            weekDay = 'Mon'
        elif day == 1:
            weekDay = 'Tue'
        elif day == 2:
            weekDay = 'Wed'
        elif day == 3:
            weekDay = 'Thur'
        elif day == 4:
            weekDay = 'Fri'
        elif day == 5:
            weekDay = 'Sat'
        else:
            weekDay = 'Sun'

        return weekDay

    # / / current date method
    def currentDate(self):
        # / / current date string
        month = str(self.month)
        day = str(self.day)
        date = month + '/' + day

        return date

    # / / new day method
    def newDay(self, lastday):
        day = self.dayOfWeek()
        if day != lastday:
            newDay = True
        else:
            newDay = False
        return newDay