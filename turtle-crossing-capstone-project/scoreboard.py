FONT = ("Courier", 24, "normal")
SCOREBOARD_LOCATION = (-280, 250)
GAMEOVER_LOCATION = (0, 0)
GAMEOVER_FONT = ("Courier", 50, "bold")


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCOREBOARD_LOCATION)
        self.write(f"Level: {self.level} ", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(GAMEOVER_LOCATION)
        self.write("GAME OVER!", align="center", font=GAMEOVER_FONT)