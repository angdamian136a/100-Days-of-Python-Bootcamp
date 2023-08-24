from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 12
        self.move_speed = 0.1


    def moving(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def wall_bounce(self):
        self.y_move *= (-1)

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.1





