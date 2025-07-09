from turtle import Turtle, Screen

# Challenge 1: Make an Etch-A-Sketch with following controls
# W - Move forward
# S - Move backward
# A - Turn Counter-Clockwise
# D - Turn Clockwise
# C - Clear the screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# To bind a keystroke to an event, we need to use an event listener
# Example: turtle.onkey(fun, key)
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
