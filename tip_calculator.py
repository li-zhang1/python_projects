#Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("what is the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
final_bill = round((bill * (1 + tip_percent/100))/people,2)
final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")
