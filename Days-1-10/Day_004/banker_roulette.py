'''
Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work,
you must enter all the names as names followed by comma then space. e.g. name, name, name

HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!

Hints
You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!
'''
import random

names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
it = random.randint(0, (len(names_string)-1))
print(f"{names_string[it]} is going to buy the meal today!")

# Instructor Solution
# import random
#
# names_string = "Angela, Ben, Jenny, Michael, Chloe"
# names = names_string.split(", ")  # converts the input name_string into an array separating each name by a comma and space.
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# print(names[random_choice])

