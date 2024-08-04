# This improves on calculator version one (calculator.py). In this update, the input operations are embedded in a 'for'
# loop to continue asking for an operation and another number until the user chooses 'n' for no.

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

calculate = operations[operand_choice]
answer = calculate(num1, num2)
print(f"{num1} {operand_choice} {num2} = {answer}")

end_function = True

while end_function:
    yes_or_no = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ")
    if yes_or_no == "y":
        old_answer = answer
        # Overwrite original operand_choice and calculate values.
        operand_choice = input("Pick another operation: ")
        new_number = int(input("What's the next number? "))
        calculate = operations[operand_choice]

        new_answer = calculate(old_answer, new_number)
        print(f"{old_answer} {operand_choice} {new_number} = {new_answer}")
        answer = new_answer
    else:
        end_function = False


#################
# Instructor Code
#################

# def add(n1, n2):
#   return n1 + n2
#
# def subtract(n1, n2):
#   return n1 - n2
#
# def multiply(n1, n2):
#   return n1 * n2
#
# def divide(n1, n2):
#   return n1 / n2
#
# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }
#
# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#     print(symbol)
# should_continue = True
#
# while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = int(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     first_answer = calculation_function(num1, num2)
#
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: " ) == "y"
#         num1 = answer
#     else:
#         should_continue = False