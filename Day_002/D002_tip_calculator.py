# DAY 2 PROJECT:
# 1. Welcome the user.
# 2. Ask for the total bill.
# 3. Ask what percentage tip (10, 12, or 15 percent.
# 4. Ask how many people to split the bill.
# 5. Output what each person should pay. Format with 2 decimal places.

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What's the total bill? $"))
tip = int(input("What percentage tip would you like to give (10, 12, or 15 percent)? "))
people = int(input("How many people to split the bill? "))

total = bill * (1 + (tip/100))
split = total / people

print(f"Each person should pay: ${round(split, 2)}.")