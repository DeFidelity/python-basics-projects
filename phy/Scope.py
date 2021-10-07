################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")
# ############### local scope #############

# def poker():
#     gbebody = 2
#     print(gbebody)
# poker()
# print(gbebody)
# #its not going to work because a variable thats created within a function can only be assesed inside that function.

# ######### GLobal Scope  #################
# playerHealth = 10
# def soul():
#     potion_strength =2
#     print(playerHealth)
# soul()
# print(playerHealth)

# ########## Modifying Global Scope

# enemies - 1
# def increase enemy():
#     # global enemies
#     # enemies += 1
#     # print(f" enemies inside the function: {enemies}")

# #   this can be achived by just typing the word global before the name enemy then calling it eithin the function. it would work out well but its not in anyway advisable to modify a global functio in a local variable
#      return enemies + 1
# #   but instead its advisable to sset the function to do that work (add one to the global varaible when ever the function is called ) like this

# enemies = increase_enemies
# print(f"enemies outside function: {enemies}")
# #global constants
# # at some points in our code we create some variable that we neve plan to change them again, for such the global variable is very very useful but its advisable to save there variable name with all Upper Case.
# PI = 2.14159
# URL = "http//www.google.com "
# TWITTER_HANDLE =  "@yu_angela"
import random

def result(computer_number, human_number):
    """ it shows the result"""
    if computer_number > human_number:
        return "number too low"
        attempt
    elif human_number > computer_number:
        return "number too high"
    elif human_number == computer_number:
        return "you're right"
def hard(attempt):
    return attempt - 5
        




print("welcome to the number Guessing Game")
print("I am thinking of a number between 1 and 100. can you guess it? ")
difficulty = print(input("choose your difficulty level. Type 'easy' or 'hard' "))
end_game = False
attempt = 10
computer_number = random.randint(1, 101)
while not end_game:
    if difficulty == "easy":
            print(f"You have {attempt} attempts ")
    elif difficulty == "hard":
            print(f"You have {hard(attempt)} attempts left")
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







