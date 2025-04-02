from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("red")

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




# Screen class shows the window, otherwise you will only see it in a brief flash.
# This stays in the bottom of the code. exitonclick method will close the window on click.
screen = Screen()
screen.exitonclick()
