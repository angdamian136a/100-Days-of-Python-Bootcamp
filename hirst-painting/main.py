import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice
colours_list = colorgram.extract('dot-image.jpg', 50)
rgb_list = []
for colour in colours_list:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb_list.append((r, g, b))

turtle.colormode(255)
tim = Turtle()
tim.shape("circle")
tim.hideturtle()
tim.speed(10)
tim.pensize(20)
tim.penup()
tim.setheading(225)
tim.forward(350)


rgb_list_refined = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

def fill_row(num_dots):
    tim.setheading(0)
    for i in range(num_dots):
        tim.dot(20, choice(rgb_list_refined))
        tim.forward(50)

def reposition(num_dots):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(num_dots*50)

def paint_hirst_style(num_dots):
    for j in range(num_dots):
        fill_row(num_dots)
        reposition(num_dots)

paint_hirst_style(10)





screen = Screen()
screen.exitonclick()


