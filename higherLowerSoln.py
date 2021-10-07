from higherLowerArt import logo,vs
from higherLowerData import data
import random
def format_data(account):
    Aname = account["name"]
    Adescription = account["description"]
    Acountry = account["country"]
    return f"{Aname}, a {Adescription}, from {Acountry} "
def compare(guess, a_follower, b_follower):
    """a check that shows who has more followers"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
account_b = random.choice(data)
score = 0
game_continue = True
print(logo)
while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")
    guess = input("Who has more follower? type A or B  ").lower()
    a_follower = account_a['follower_count']
    b_follower = account_b['follower_count']

    is_correct = compare(guess, a_follower, b_follower)
    print(logo)
    if is_correct:
        score += 1
        print(f"You're Right, your current is {score}")
    else:
        game_continue = False
        print(f"You're wrong, your score is {score} ")




