import random
from numberGuesingArt import logo2
HARD_ATTEMPT = 5
EASY_ATTEMPT = 10
def result(computer_number, human_number):
    """ it shows the result"""
    if computer_number > human_number:
        return "number too low"
        attempt
    elif human_number > computer_number:
        return "number too high"
    elif human_number == computer_number:
        return "you're right"
def difficulty():
    """sets the difficulty of the game and retuns the number of attempt"""
    difficulty = input("choose your difficulty level. Type 'easy' or 'hard' ")
    if difficulty == "easy":
            return EASY_ATTEMPT
    elif difficulty == "hard":
            return HARD_ATTEMPT
    else:
        print("your input is incorrect")
        



print(logo2)
print("welcome to the number Guessing Game")
print("I am thinking of a number between 1 and 100. can you guess it? ")

end_game = False
attempt = difficulty()
print(f"you have {attempt} attempts remaining to guess the number. ")
computer_number = random.randint(1, 101)
while not end_game:
    human_number = int(input("Make a guess "))
    if result(computer_number, human_number) == "you're right":
        end_game = True
        print("you win")
    else:
        attempt -= 1
        print(result(computer_number,human_number))
        print(f"you have {attempt} attempt left ")
    if attempt == 0:
        end_game = True


