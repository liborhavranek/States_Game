import pandas
import turtle
from turtle import *


data = pandas.read_csv("50_states.csv")

my_screen = Screen()
my_screen.title(f"States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)
# -------------------------------------------------------
# def get_mouse_click_coor(x, y):
# 	"""This function take coordinates from my_screen"""
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# ----------------------------------------------------------

state_list = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
	user_answer = my_screen.textinput(title=f"{len(guessed_state)}/{len(data.state)}", prompt="Guess state").title()
	if user_answer == "Exit":
		missing_states = []
		for state in state_list:
			if state not in guessed_state:
				missing_states.append(state)
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("missing_states.csv")
		print(missing_states)
		break
	if user_answer in state_list:
		guessed_state.append(user_answer)
		right_answer = Turtle()
		right_answer.hideturtle()
		right_answer.penup()
		coordinate = data[data.state == user_answer]
		right_answer.goto(int(coordinate.x), int(coordinate.y))
		right_answer.write(coordinate.state.item())
