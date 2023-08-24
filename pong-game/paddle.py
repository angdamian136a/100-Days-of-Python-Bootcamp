from turtle import Turtle
MOVE_DISTANCE = 30

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.goto(starting_position)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


