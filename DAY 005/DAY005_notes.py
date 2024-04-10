#############
# for loop
#############
"""
Syntax:
for item in list_of_items:
    # Do something to each item
"""
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

################################
# for loops and range() function
################################
"""
Syntax:
for number in range(a, b):
    print(number)
"""
# Example 1
for number in range(1, 10, 2):  # between 1 and 10, starting at 1 but NOT including 10. Optional third argument
    print(number)               # is for step. In this case, this will print in increments by 2 (1, 3, 5, 7, 9).

#Example 2
total = 0
for number in range(1, 101):
    total += number
print(total)