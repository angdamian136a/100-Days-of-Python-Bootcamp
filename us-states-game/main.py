import turtle
from state_namer import StateNamer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas as pd
all_states_data = pd.read_csv("50_states.csv")
state_names_list = all_states_data["state"].to_list()
xcors_list = all_states_data["x"].to_list()
ycors_list = all_states_data["y"].to_list()

state_names_cors_dict = {}
for i in range(len(state_names_list)):
    state_names_cors_dict[state_names_list[i]] = (xcors_list[i], ycors_list[i])
# print(state_names_cors_dict)

state_namer = StateNamer()
correct_guesses_list = []

TITLE = "Guess the US State"
while len(correct_guesses_list) < 50:
    answer_state = screen.textinput(title= TITLE, prompt="What's another state?").title()
    if answer_state == "Exit":
        states_to_learn_list = [state for state in state_names_list if state not in correct_guesses_list]
        # states_to_learn_list = []
        # for state in state_names_list:
        #     if state not in correct_guesses_list:
        #         states_to_learn_list.append(state)
        new_data = pd.DataFrame(states_to_learn_list)
        new_data.to_csv("states_to_learn.csv")
        break
    for name in state_names_cors_dict:
        state_cors = state_names_cors_dict[name]
        if answer_state == name:
            state_namer.correct_state_name(state_cors, name)
            correct_guesses_list.append(name)
    TITLE = f"{len(correct_guesses_list)}/50 states correct"

# states_to_learn_list = state_names_list
# for name in correct_guesses_list:
#     states_to_learn_list.remove(name)
# df = pd.DataFrame(states_to_learn_list)
# df.to_csv("states_to_learn.csv")

