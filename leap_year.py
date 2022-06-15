# Chcek whether a particular year is a leap year.
# Flow chart to help solve this problem: https://bit.ly/36BjS2D
year = int(input("Which year do you want to check? "))

if year == 4:
    if year == 100:
        if year == 400:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.")

# Another solution
year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 != 0:
    print("Not leap year.")
else:
    print("Leap year.")


