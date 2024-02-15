from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# colours = ["violet", "indigo", "blue", "green", "gold2", "orange", "red"]
directions = [0, 90, 180, 270]
thick = [0, 2, 4, 6, 8]
timmy = Turtle()
timmy.shape("turtle")
timmy.screen.bgcolor("skyblue")
timmy.speed("fastest")

for _ in range(150):
    timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
    timmy.width(random.choice(thick))

screen = Screen()
screen.exitonclick()
