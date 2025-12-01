from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT_SIZE = 15
FONT_TYPE = "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")   # Text default is black
        self.penup()
        self.goto(0, 280)
        self.refresh_scoreboard()
        self.hideturtle()   # Hides turtle and leaves only the text created in self.write

    def refresh_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_TYPE))

    def add_point(self):
        self.score += 1
        self.clear()   # Clear previous text written on scoreboard
        self.refresh_scoreboard()