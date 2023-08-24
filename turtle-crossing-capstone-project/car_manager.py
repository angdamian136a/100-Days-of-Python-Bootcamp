COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 25
ROAD_WIDTH = 500
NUM_LANES = int(ROAD_WIDTH/LANE_WIDTH)
ROAD_LOWER_BOUND = -250

#TODO: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the
# left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a
# safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck,
# check the video walkthrough in Step 4.

from turtle import Turtle
import math
import random

y_cor_list = []
y_cor_count = 0
for i in range(NUM_LANES):
    y_cor_count = ROAD_LOWER_BOUND + i*LANE_WIDTH + LANE_WIDTH/2
    y_cor_list.append(math.ceil(y_cor_count))

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(COLORS[random.randint(0, len(COLORS)-1)])
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(280, y_cor_list[random.randint(0, NUM_LANES - 1)])
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
