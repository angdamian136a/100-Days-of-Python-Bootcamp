STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#TODO: Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the
# turtle north. If you get stuck, check the video walkthrough in Step 3.

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False




