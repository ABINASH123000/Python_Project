'''This is a game.In this game a person chooses how man turn they want and roll dice and if dice value is other than 1 then the value added until its value reaches the wining value'''
import random


def play():
    user_value = 0
    num_of_chances = int(input("Enter How Many Chances:"))
    while num_of_chances >= 0:
        x = input("press any key and enter  to continue")
        dice_value = random.randrange(1, 7)

        if dice_value == 1:
            print("you lose 1 appered!!!")
            return 0
        elif user_value == 50:
            print("you win")
            return 0
        elif x.lower() == exit:
            return 0
        else:
            user_value += dice_value
            print("Your total score:"+str(user_value))

        num_of_chances -= 1


play()
