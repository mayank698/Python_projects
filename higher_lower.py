from higher_lower_data import data
import random
from higher_lower_art import logo, vs
import os


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the users answer and check whether they are right or wrong."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more follower 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"You are right.Current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score is {score}")
