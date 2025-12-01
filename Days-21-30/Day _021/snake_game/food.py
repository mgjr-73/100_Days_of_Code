from turtle import Turtle
import random

# Challenge 1.1: Adding Turtle as argument for class Food allows food to inherit attributes and methods from Turtle.
class Food(Turtle):
    def __init__(self):
        # Challenge 1.2: After adding Turtle as argument, step 2 is to initialize Turtle attributes and methods.
        super().__init__()
        # The following attributes are from Turtle class, thanks to inheritance.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)