"""
this program is to store and manipulate the days of the week.
"""

class WeekDayError(Exception):
    pass
	
class Weeker:
    days = ['Mon','Tue', 'Wed' ,'Thu','Fri','Sat','Sun']

    def __init__(self, day):
        self.__day = day
        if self.__day not in Weeker.days:
            raise WeekDayError
        
    def __str__(self):
        return self.__day

    def add_days(self, n):
        n = n % 7
        self.__day = Weeker.days[(Weeker.days.index(self.__day) + n) % 7]
        
    def subtract_days(self, n):
         n = n % 7
         self.__day = Weeker.days[(Weeker.days.index(self.__day) - n)]
         
         
         


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
