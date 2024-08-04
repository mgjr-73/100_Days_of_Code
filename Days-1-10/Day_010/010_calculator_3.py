# This improves on calculator version 2 (calculator_2.py). In this update, the use can start a fresh calculator instead
# of just exiting the loop and ending the program. This is done by the use of 'Recursion', where a function can
# call itself.
# We do this here by putting the code into a calculator function.
from os import system, name
from calc_logo import logo


def clear():
    """Emulate the 'clear screen' command based on the current OS"""
    if name == 'nt':   # for Windows
        _ = system('cls')
    else:   # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

# Calculator
def add(n1, n2):
    """Add n1 and n2"""
    return n1 + n2

def subtract(n1, n2):
    """subtract n1 from n2"""
    return n1 - n2

def multiply(n1, n2):
    """multiply n1 with n2"""
    return n1 * n2

def divide(n1, n2):
    """divide n1 by n2"""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operand in operations:
        print(operand)
    end_function = True

    while end_function:
        operand_choice = input("Pick an operation symbol from above: ")
        # 'int' was changed to 'float' to allow for floating point numbers
        num2 = float(input("What's the second number?: "))
        calculate = operations[operand_choice]
        answer = calculate(num1, num2)

        print(f"{num1} {operand_choice} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation: ") == "y":
            num1 = answer
        else:
            end_function = False
            clear()
            calculator()


calculator()

