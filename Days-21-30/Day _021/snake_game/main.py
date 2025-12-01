import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Refer to main_a.py to see how we implemented OOP.

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Moving the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.snake_move()

    # Detect collision with food using turtle.distance method
    if snake.head.distance(food) < 15:
        food.refresh_food_location()
        snake.grow_snake()
        scoreboard.add_point()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
