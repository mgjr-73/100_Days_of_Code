import turtle
from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
# tim.color("red")
turtle.colormode(255)

# Challenge 1 - Draw a Square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

# Challenge 1 Solution
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# import heroes
# print(heroes.gen())

# Challenge 2 - Draw Dashed Line
# for _ in range(10):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

# Challenge 2 Solution
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3 - Draw Shapes
# full = 360
# tim.forward(50)
# for x in range(3, 37):
#     if (full % x) == 0:
#         angle = int(full/x)
#         for _ in range (x):
#             tim.right(angle)
#             tim.forward(50)

# Challenge 3 Solution

# import random
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# Challenge 4 - Random Walk
# - Turtle walks randomly in any of the four directions, N, E, S, W
# - Line changes color at every step
# - Make lines thicker
# - Make turtle draw faster

import random


# heading = [0, 90, 180, 270]
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def turtle_move():
#     step_heading = random.choice(heading)
#     tim.speed(10)
#     tim.pensize(10)
#     tim.forward(50)
#     tim.setheading(step_heading)
#
#
# while True:
#     tim.color(random.choice(colors))
#     turtle_move()


# Challenge 4 Solution
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Eliminating set of colors and instead use r, g, b.
# Up above, we commented out tim.color and replaced it with Turtle.colormode(255). 255 represents the upper limit of
# the color range.

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

    # instructor solution, assign RGB to variable random color then return.
    # I just did a shortcut.
    # random_color = (r, g, b)
    # return random_color

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# CHALLENGE 5: Draw a Spirograph
# - Learn how to draw circle
# - Learn how to draw it repeatedly while changing the tilt up to 360 degrees to complete the spirograph

tim.speed("fastest")
#
# for a in range(0, 361, 1):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(a)

# Instructor solution
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)

# Screen class shows the window, otherwise you will only see it in a brief flash.
# This stays in the bottom of the code. exitonclick method will close the window on click.
screen = Screen()
screen.exitonclick()
