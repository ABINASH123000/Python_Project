import random


def guess_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    correct_guess = ""
    word = random.choice(words)
    chances = random.randrange(1, len(word))
    initial = 0
    while True:
        if correct_guess == word:
            print(f"You guessed correct: {correct_guess}")
            return 0
        else:
            user_char = input("You have" + str(chances) + "chances." +
                              "Guess the charatecter of" + str(len(word)) + "word")
            if user_char == word[initial]:
                initial += 1
                correct_guess += user_char
                print(f"{correct_guess} "+"_"*(len(word)-(initial)))
            elif chances == 0:
                print("You lose")
                return 0
            elif user_char != word[initial]:
                chances -= 1
                print(f"Wrong! Try again")
            else:
                print("Error!!!")


guess_word()
