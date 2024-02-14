import random
import os
from blackJack_art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of card a returns the scores calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and cards == 11:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the score of user and computer."""
    if computer_score == user_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Lose, opponent has a black jack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You are over 21.Opponent win."
    elif computer_score > 21:
        return "Opponent over 21. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():

    print(logo)

    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    is_game_over = False

    while not is_game_over:

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards are {user_card}, your score is {user_score}")
        print(f"Computers card is {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:

            users_choice = input(
                "Type 'y' to get another card, type 'n' to exit: ")
            if users_choice == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand is {user_card}, final score:{user_score}")
    print(f"Computers final hand is {computer_card}, final score:{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of blackJack? Type 'y' otherwise type 'n': ") == 'y':
    os.system('cls')
    play_game()
