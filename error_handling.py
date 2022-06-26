"""
This programme is to write a function able to input integer values 
and to check if they are within a specified range.
"""


def read_int(prompt, min, max):
    try:
        num = int(input(prompt))
        if(num > 10 or num < -10):
            raise Exception
        return num
    except ValueError:
        print("Error: wrong input")
        quit()
    except Exception:
        print(f"Error: the value is not within permitted range ({min}..{max})")
        quit()
        
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)