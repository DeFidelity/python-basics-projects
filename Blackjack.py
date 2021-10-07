import random
import blackjackArt
from blackjackArt import logo
def deal_card():
    """Sends out a random number from cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """takes a list of cards and sum them up"""
#   or if 11 in cards and 10 in card and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack 🤪 "
    elif user_score == 0:
        return "You win with a black jack 🤩 "
    elif user_score > 21:
        return " You went over score 🤨 "
    elif computer_score > 21:
        return "Opponent went over score, You win 😝 😜 "
    elif user_score > computer_score:
        return "you win 😝"
    else:
        return "You lose 🤨 "
def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} and current score is {user_score}")
        print(f" Computer's first card is {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            draw_card = input("do you want to draw another card? typr 'y' for yes and 'n' for no \n")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" your final hand is {user_cards} and your final score is {user_score} and computer score is {computer_score} ")
    print(compare(user_score, computer_score))
while input("Do you want to play BlackJack? type 'y' for yes and 'n' for no:  ") == "y":
    blackjack()


