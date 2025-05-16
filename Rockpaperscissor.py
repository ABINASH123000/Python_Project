# rock paper scissor
import random as random


def play():
    user_input: str = input(f"select from {option}")
    computer_input: str = random.choice(option)
    print(f"your:{user_input} computer:{computer_input}")
    if user_input == computer_input:
        return "Draw"
    elif win.get(computer_input) == user_input.lower:
        return "User Wins"
    else:
        return "computer Wins"


option: list = ("rock", "paper", "scissor")
win: dict = {
    "rock": "paper",
    "paper": "scissor",
    "scissor": "rock",
}
number_of_play = int(input("No of time You want to play"))
while (True):

    print(play())
    if number_of_play == 0:
        break
    else:
        number_of_play -= 1
