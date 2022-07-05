"""
Use recursion to wirte a calculator in Python
"""
from art import logo
import os
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    to_continue = True
    while to_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        option = input(f"1. Type 'y' to continue calculating with {result}.\n2. type 'r' to start a new calculation.\n3. type 'n' to exit.\n")
        if option == 'y':
            num1 = result
        elif option == 'r':
            to_continue = False
            calculator()
            os.system('clear')
        else:
            to_continue = False
calculator()




