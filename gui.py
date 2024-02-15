from turtle import Turtle, Screen
import random

colours = ["violet", "indigo", "blue", "green", "gold2", "orange", "red"]

timmy = Turtle()
timmy.shape("turtle")


def draw_shapes(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.left(angle)


for i in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shapes(i)

screen = Screen()
screen.exitonclick()
