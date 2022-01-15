import turtle
import time
from states_config import Coords

screen = turtle.Screen()
# Instance from the coordinates class in states_config file
coords = Coords()

# Map selection
map_selection = screen.textinput(title="map", prompt="Which Map do you want to guess MX/US?").upper()
if map_selection == "MX":
    data, states, image,  resolution, title, max_states = coords.assign_info(1)
else:
    data, states, image, resolution, title, max_states = coords.assign_info(2)

screen.title(title)
screen.addshape(image)
screen.setup(width=resolution[0], height=resolution[1])
turtle.shape(image)
screen.tracer(0)

# Start The Game
states_already_guessed = []
while True:
    time.sleep(0.1)
    screen.update()
    counter = len(states_already_guessed)
    answer_state = screen.textinput(title=f"{counter}/{max_states} States Correct", prompt="What's another state's name?").title()
    if counter == max_states or answer_state == "Exit":
        break
    elif answer_state in states and answer_state not in states_already_guessed:
        states_already_guessed.append(answer_state)
        state = data[data["state"] == answer_state]
        coords.go_to(state, answer_state)

if answer_state == "Exit":

    # Remove from states the guessed states
    for _ in states_already_guessed:
        if _ in states:
            states.remove(_)

    # Once the user type Exit, set the failed states in the screen
    for name in states:
        state = data[data["state"] == name]
        coords.hideturtle()
        coords.go_to(state, name, "red")
else:
    turtle.write("YOU WIN!!!!!")

coords.score(states, states_already_guessed)



screen.exitonclick()
