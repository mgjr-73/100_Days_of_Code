from os import system, name


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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for operand in operations:
    print(operand)
operand_choice = input("Pick an operation symbol from above: ")

calculate = operations[operand_choice](num1, num2)
print(f"{num1} {operand_choice} {num2} = {calculate}")


###############################
# Instructor Code for calculate
###############################

# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")