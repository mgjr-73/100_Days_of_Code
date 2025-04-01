from turtle import Turtle, Screen


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Challenge 1 - Draw a Square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# Challenge 1 Solution
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)


import heroes
print(heroes.gen())


# Screen class shows the window, otherwise you will only see it in a brief flash.
# This stays in the bottom of the code. exitonclick method will close the window on click.
screen = Screen()
screen.exitonclick()
