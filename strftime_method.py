"""
This program is to represent the different format of datetime
by using strftime method.
datetime : https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
time: https://docs.python.org/3/library/time.html#time.strftime

"""

from datetime import datetime

d = datetime(2020,11,4,14,53)
print(d)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print(d.strftime("weekday: %w"))
print(d.strftime("Day of the year: %j"))
print(d.strftime("Week number of the year: %U"))
