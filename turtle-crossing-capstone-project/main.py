import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Capstone Project")
screen.listen()

player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
count = 0
car_list = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    if player.level_up():
        player.go_to_start()
        car_manager.speed_up()
        scoreboard.increase_level()



screen.exitonclick()

