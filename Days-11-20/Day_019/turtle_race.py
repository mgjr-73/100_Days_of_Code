import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
# Set size of screen in pixels
screen.setup(width=500, height=400)
# Ask user to bet on a turtle color
user_bet = screen.textinput(title="Bet on a color", prompt='Pick a turtle to bet on ("red", "orange", "yellow", "green", "blue", "purple"): ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle won!")
            else:
                print(f"{winning_color} turtle won. Your {user_bet} turtle lost.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()