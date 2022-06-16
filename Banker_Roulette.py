"""
This program is to select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
"""

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

rand = random.randint(0,len(names)-1)
person_who_will_pay = names[rand]

print(f"{person_who_will_pay} is going to buy the meal today!")
