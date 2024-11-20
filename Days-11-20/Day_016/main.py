## Call the turtle module, use its Turtle class and assign it to an object called timmy
## The parenthesis after Turtle is needed to simply initialize the object
# import turtle
import turtle
# An even simple way of using Turtle class is:
from turtle import Turtle, Screen

# Then you can simply assign it to the object as:
timmy = Turtle()
print(timmy)
# Change timmy's shape from the default arrow into a turtle by calling the 'shape' method
timmy.shape("turtle")
# Change timmy's color using the 'color' method
timmy.color("blue1")
# Make timmy move forward 100 spaces with the 'forward' method
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

# A method within the Screen class
my_screen.exitonclick()

