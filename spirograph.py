from turtle import Turtle, Screen
import random
import turtle


turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + 10)
        timmy.circle(100)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
