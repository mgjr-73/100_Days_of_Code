#######################################
# Defining and Calling Python Functions
#######################################
# https://docs.python.org/3/library/functions.html

# To create our own function, we need to define it with keyword 'def'
"""
Syntax:
def my_function():
    # Do this
    # Then do this
    # Finally do this
"""
def my_function():
    print("Hello")

my_function()  # This is called calling the function.

#################################
# Hurdles Loop Challenge Solution
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for n in range(6):
    hurdle()

######################
# Indentation
######################

# Indentation standard is 4 spaces to the right.
# Refer to https://peps.python.org/pep-0008/

########################
# While loops
########################

while test_condition_if_it_resolves_to_True:
    # Do something repeatedly until condition is met
`   # BEWARE of infinite loops!

# Hurdle challenge 2: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not front_is_clear():
        hurdle()
    else:
        move()

# Hurdle Challenge 3: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if not front_is_clear():
        turn_left()
        hurdle()
    else:
        move()

#############################
# Project: Escaping the Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#############################
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and not right_is_clear():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
    else:
        move()

######################
# Instructor solution:
######################
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# NOTE: This instructor solution may encounter infinite loop if robot starts at an open area in the map.
# My solution worked perfectly for all given problem starts.