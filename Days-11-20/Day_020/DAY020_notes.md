# Tips
- Break down the problem
  - Create a snake body
  - Move the snake
  - Control the snake
  - Detect collision with food
  - Create a scoreboard
  - Detect a collision with wall
  - Detect collision with tail

# Screen Setup and Creating a Snake Body
## Challenge 1:
Create 3 white turtles with a square shape and position them in a line with the first one at 0,0
and adding the next one to the left of it and so on. A unit of square is 20x20 px.
### My solution
```python
x_pos = 0
for snake_index in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_pos, y=0)
    x_pos = x_pos-20
```
### Instructor solution
```python
# Simple
segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40, 0)

# Using for loop
starting_positions = [(0,0), (-20,0), (-40,0)]
for position in starting_positions:
   new_segment = Turtle("square")
   new_segment.color("white")
   new_segment.goto(position)
```


# Animating the Snake Segments on Screen
- See `tracer` and `update` methods in Turtle documentation
    ```python
    # Instructor added block.
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(1)
    
        # The idea here is to for the middle and the tail segments to follow the head.
        # This is achieved by starting with the tail (segment 3) going to the middle's 
        # coordinates. Then the middle (segment 2) going to the head's coordinate, and 
        # then the head (segment 0) moving to a new coordinate.
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
    ```

# Create a Snake class & Move to OOP
- Refactor to have three classes
  - Snake
  - Food
  - Scoreboard
- Create a file named snake.py to handle the creation of the snake and then import it to main.

# How to Control the Snake with a Keypress
- We use screen methods `.listen()` and `.onkey()`
    ```python
    # Moving the snake
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    ```
- Notice we're calling up, down, left, right from Snake class.
    ```python
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    ```
  
# TIP
Programming is not about memorizing. You have Google and/or AI to search for the correct function or syntax. You job is
to understand how things work. Understand how and when to use the code.