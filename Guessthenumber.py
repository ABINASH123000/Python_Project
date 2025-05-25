import random


def guess():
    random_number = random.randrange(1, 100)
    chance = random.randrange(1, 10)
    for i in range(1, chance+1):
        user_guess = int(
            input(f"Guess  The number between 1-100 in {chance} chances"))
        if user_guess == random_number:
            print("You guessed corrected")
            return 0
        elif i < chance and user_guess > random_number:
            print("wrong guessed too high!  try again!!")
        elif i < chance and user_guess < random_number:
            print("wrong guessed too low! try again!!")
        elif i == chance:
            print("you lose")


guess()
