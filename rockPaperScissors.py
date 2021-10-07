import random
gameImages = [rock, paper, scissors]
print("Welcome to the Rock paper scissors game")
usersChoice = int(input("what do you chose? type 0 for rock, 1 for paper or 2 for scissors.\n " ))
print(gameImages[usersChoice])
computer = random.randint(0, 2)
print(f"computer choose: ")
print(gameImages[computer])
print
if usersChoice >= 3 or usersChoice < 0:
    print("You typed an invalid number, you lose!")
elif computer == 2 and usersChoice == 0:
    print("you win")
elif computer == 0 and usersChoice == 2:
    print("you lose")
elif computer > usersChoice:
    print("you lose")
elif usersChoice > computer:
    print("you win")
elif computer == usersChoice:
    print("its draw")


    
    
