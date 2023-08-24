from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        # if not self.check_high_score():
        #     with open("data.txt", "r") as file:
        #         old_high_score = int(file.read())
        #         self.high_score = old_high_score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def record_high_score(self):
    #     with open("data.txt", mode="w") as file:
    #         file.write(f"{self.high_score}")

    # def check_high_score(self):
    #     with open("data.txt", mode="r") as file:
    #         recorded_high_score = int(file.read())
    #         if self.high_score > recorded_high_score:
    #             self.record_high_score()
    #         else:
    #             return False



