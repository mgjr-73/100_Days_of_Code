import time
from turtle import Screen, Turtle


# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)   # This will only show a blank screen until we call the 'update' method.

segments = []   # instructor added
# Challenge 1. See notes.
x_pos = 0
for snake_index in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_pos, y=0)
    x_pos = x_pos-20
    segments.append(snake)   # instructor added

# Instructor added block.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)






screen.exitonclick()