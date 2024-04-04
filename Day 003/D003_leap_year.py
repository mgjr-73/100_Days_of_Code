'''
Write a program that works out whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February.

This is how you work out whether if a particular year is a leap year:
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder


'''
year = 2020

# Value check
cond1 = year % 4 # no remainder, leap year
cond2 = year % 100 # no remainder, not leap year
cond3 = year % 400 # no remainder, leap year
print(cond1, cond2, cond3)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")

# Instructor Solution
print()
print("Instructor Solution:")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year")