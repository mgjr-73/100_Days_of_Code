# Final project: create 10 x 10 spots with turtle using the color palette
# Each dot should be size 20, and spaced at 50.
import turtle
from turtle import Turtle, Screen
import random


# Enable use of rgb numeric values for color
turtle.colormode(255)

# Set canvas size
turtle.screensize(1000, 1000)
print(f"canvas size = {turtle.screensize()}")

tim = Turtle()

# Hide turtle
tim.hideturtle()

# Set start position
tim.penup()
start_x = -400.00
start_y = -400.00
tim.goto(start_x, start_y)
print(f"starting position = {tim.pos()}")

# Set speed
tim.speed("fastest")

# Output from running extract_color.py
color_palette = [(218, 219, 214), (233, 235, 239), (212, 155, 87), (213, 221, 215), (220, 205, 108), (224, 209, 214),
                 (187, 82, 46), (133, 144, 28), (221, 77, 128), (41, 122, 73)]

def tim_move(num_dots):
    for _ in range(num_dots):
        tim.dot(20, dot_color())
        tim.penup()
        tim.forward(50)

def dot_color():
    color = random. choice(color_palette)
    r = color[0]
    g = color[1]
    b = color[2]
    rgb_color = (r, g, b)
    return rgb_color


y = start_y
dots_per_line = 17

for _ in range(dots_per_line):
    tim.teleport(start_x, y)
    tim_move(dots_per_line)
    y += 50

# Screen class shows the window, otherwise you will only see it in a brief flash.
# This stays in the bottom of the code. exitonclick method will close the window on click.
screen = Screen()
screen.exitonclick()



# INSTRUCTOR SOLUTION
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()












