from turtle import Turtle, Screen


screen = Screen()
# Set size of screen in pixels
screen.setup(width=500, height=400)
# Ask user to bet on a turtle color
screen.textinput(title="Bet on a color", prompt="Pick a turtle to bet on (R, O, Y, G, B, V): ")

red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
violet = Turtle()



screen.exitonclick()