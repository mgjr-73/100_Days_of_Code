# if / else statement
'''
if condition:
    run this code
else:
    run this code instead
'''
number = int(input("Enter a number: "))

if (number % 2) == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# ======================================
# Nested if / else
# ======================================
'''
if condition:
    if nested condition:
        run this nested code
    else:
        run this nested code
else:
    run this code instead
'''
print("Welcome to the rollercoaster ride!")
adult_tix = 14
minor_tix = 7

height = int(input("What is your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 18:
        print(f"Your ticket price is ${minor_tix}.")
    else:
        print(f"Your ticket price is ${adult_tix}.")
else:
    print("You cannot ride the rollercoaster.")

# ======================================
# if / elif /else
# ======================================
'''
if condition1:
    do A
elif condition2:
    do B
else:
    do this if condition 1 and 2 are not met
'''
print("Welcome to the rollercoaster ride!")
tier3_tix = 14
tier2_tix = 10
tier1_tix = 7

height = int(input("What is your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print(f"Your ticket price is ${tier1_tix}.")
    elif age < 18:
        print(f"Your ticket price is ${tier2_tix}.")
    else:
        print(f"Your ticket price is ${tier3_tix}")
else:
    print("You cannot ride the rollercoaster.")

# ======================================
# Multiple if Statements in Succession
# ======================================
'''
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C

If all conditions are True, all code will be executed.
'''
print("Welcome to the rollercoaster ride!")
tier3_tix = 14
tier2_tix = 10
tier1_tix = 7
bill = 0
height = int(input("What is your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = tier1_tix
        print(f"Your ticket price is ${bill}.")
    elif age < 18:
        bill = tier2_tix
        print(f"Your ticket price is ${bill}.")
    else:
        bill = tier3_tix
        print(f"Your ticket price is ${bill}")

    add_photo = input("Do you want add a photo for $3 (y/n)? ")
    if add_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the rollercoaster.")

# ======================================
# Logical Operators
# ======================================

A and B
C or D
not E (may be used to reverse boolean result)

print("Welcome to the rollercoaster ride!")
tier3_tix = 14
tier2_tix = 10
tier1_tix = 7
bill = 0
height = int(input("What is your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = tier1_tix
        print(f"Your ticket price is ${bill}.")
    elif age < 18:
        bill = tier2_tix
        print(f"Your ticket price is ${bill}.")
    elif age < 45:
        bill = tier3_tix
        print(f"Your ticket price is ${bill}")
    elif age == 45 or age <= 55:
        print(f"Your ticket price is ${bill}")

    add_photo = input("Do you want add a photo for $3 (y/n)? ")
    if add_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the rollercoaster.")