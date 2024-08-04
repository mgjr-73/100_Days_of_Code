#==================
# Randomization
#==================
'''
For documentation on random module, go to askpython.com
'''
import random

random_integer = random.randint(1, 10)
print(random_integer)  # prints random number within range 1 - 10.

random_float = random.random()
print(random_float)  # By default, only range from 0.00000... to 0.99999...
print(random_float * 5)  # Expands float to higher numbers, in this case from 0.00000... to 4.99999...

#==================
# Lists
#==================
'''
See docs.python.org/3/tutorial/datastructures.html
'''
us_states = ["Maryland", "New York", "Delaware"]

print(us_states[0])  # Accessing list by index number

first,second,third = us_states  # This is unpacking the list and assigning items to positional variables
print(second)

print(us_states[2])
us_states[2] = "Deelaware"  # Changes value at index number 2.
print(us_states[2])

us_states.extend(["California", "Texas", "Utah"])
print(us_states)

# Avoid getting typical off-by-one errors. Just remember list index always starts at 0.

#==================
# Nested Lists
#==================
mixed_list = [["Bob", "Sue", "John"],[8, 6, 10]]
print(mixed_list)

names = ["Bob", "Sue", "John"]
sizes = [8, 6, 10]
mixed = [names, sizes]
print(mixed)
print(mixed[0][0],mixed[1][0])