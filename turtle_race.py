from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle wins the race? Enter a color: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "red"]
all_turtles = []

y_positions = [-70, -40, -10, 20, 50, 80, 110]

# Creating turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# Checking winner by end point on x-axis 230
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print(f"You've lost! The winning color is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
