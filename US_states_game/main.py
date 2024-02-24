import turtle
import pandas

screen = turtle.Screen()
screen.title("US state game")
image = "US_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("US_states_game/50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # Using list comprehension
        missing_states = [state for state in all_states if state not in guessed_state]

        # Using normal loop
        
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states-to-learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
