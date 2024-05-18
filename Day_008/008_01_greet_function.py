# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greeting():
    print(f"Hello!")
    print("This is a function demo!")
    print("Goodbye!")
    print()


greeting()

# Function that allows input.
def greeting_with_name(name):    # "Bob" is assigned to variable 'name'.
    print(f"Hello, {name}!")
    print(f"This is a function with input: {name}")
    print("Goodbye!")
    print()


greeting_with_name("Bob")

# Function with more than one input.
def greeting_with_food(name, drink, food):
    print(f"Hello, {name}!")
    print(f"Your favorite combination is {drink} with {food}.")
    print(f"This is a function with multiple inputs.")
    print("Goodbye!")
    print()


greeting_with_food("Bob", "coffee", "bagel") # Note that these are POSITIONAL arguments.


def greeting_with_keywords(name, drink, food):
    print(f"Hello, {name}!")
    print(f"Your favorite combination is {drink} with {food}.")
    print(f"This is a function with multiple inputs.")
    print("Goodbye!")
    print()


greeting_with_food(drink="coffee", name="Bob", food="bagel") # Note that these are KEYWORD arguments.
