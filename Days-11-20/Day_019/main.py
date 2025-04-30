from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# To bind a keystroke to an event, we need to use an event listener
# Example: turtle.onkey(fun, key)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()