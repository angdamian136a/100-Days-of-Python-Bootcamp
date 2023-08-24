STATE_NAME_FONT = ("arial", 15, "normal")

from turtle import Turtle

class StateNamer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def correct_state_name(self, cors, state_name):
        self.goto(cors)
        self.write(state_name, align="center", font=STATE_NAME_FONT)