import random
from numbergame_art import logo
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, guessed_number, turns):
    if user_guess > guessed_number:
        print("Too high.")
        return turns-1

    elif user_guess < guessed_number:
        print("Too low.")
        return turns-1

    else:
        print("You got that right.")


def set_difficulty():
    level = input("Select your level 'easy' or 'hard': ").lower()
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    os.system('cls')
    print(logo)
    print("I am thinking of a number between 0 and 100.")
    guessed_number = random.randint(0, 100)
    turns = set_difficulty()
    user_guess = 0
    while guessed_number != user_guess:
        print(f"You have {turns} attempts remaining.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, guessed_number, turns)
        if turns == 0:
            print("You have no attempts left.")
            return


game()
