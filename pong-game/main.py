from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
LEFT_PADDLE_START = (-350, 0)
RIGHT_PADDLE_START = (350, 0)


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()

left_paddle = Paddle(LEFT_PADDLE_START)
right_paddle = Paddle(RIGHT_PADDLE_START)

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

scoreboard = Scoreboard()

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.moving()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -322 or ball.distance(right_paddle) < 50 and ball.xcor() > 322:
        ball.paddle_bounce()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_win()
        scoreboard.score_update()

    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_win()
        scoreboard.score_update()


screen.exitonclick()

