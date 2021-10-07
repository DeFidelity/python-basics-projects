import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    from random import shuffle
    shuffle(cards)
    ret = cards[:2]
    return ret

user = []
computer = []
deal_card().append(user)
deal_card().append(computer)

def calculate_score(cards):
    import math
    return sum(cards)
    if 10 in cards:
        return 0
    elif 11 in cards:
        if sum() > 21:
            remove(cards)
            append(cards)
        elif sum < 21
            return 11
    

calculate_score():
if calculate_score() == 0:
    print("game over")
elif user or computer > 21:
    print("game over")
else:
    if input("Do you wasnt to draw another card? type 'yes' or 'no' " ) == yes:
        random.choice(deal_card).append(user)
    else:
        print("Game over")













