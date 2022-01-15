from turtle import Turtle, Screen
import pandas
screen = Screen()


class Coords(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.resolution = [0, 0]
        self.title = ""
        self.url = ""
        self.max_states = 0
        self.image = ""
        self.data = ""
        self.states = ""

    def go_to(self, state, answer_state, color="black"):
        x = int(state.x)
        y = int(state.y)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.write(answer_state)

    def score(self, states, states_already_guessed):
        self.goto(-420, 230)
        self.write(f"missed = {len(states)}")
        self.color("black")
        self.goto(-420, 220)
        self.write(f"correct = {len(states_already_guessed)}")

    def assign_info(self, res):
        if res == 1:
            self.url = "mx_states.csv"
            self.data = pandas.read_csv(self.url)
            self.states = self.data["state"].to_list()
            self.image = "image/mexico.gif"
            self.resolution = [1414, 924]
            self.title = "Mexico States Game"
            self.max_states = 32
        elif res == 2:
            self.url = "50_states.csv"
            self.data = pandas.read_csv(self.url)
            self.states = self.data["state"].to_list()
            self.image = "image/blank_states_img.gif"
            self.resolution = [850, 500]
            self.title = "U.S. States Game"
            self.max_states = 50
        return self.data, self.states, self.image, self.resolution, self.title, self.max_states



