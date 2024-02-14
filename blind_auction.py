import os
from auction_art import logo


bidding = {}

print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for each_bidder in bidding_record:
        bid_amount = bidding_record[each_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = each_bidder
    print(f"The winner is {winner} with the highest bid of {highest_bid}")


any_other_bidder = True
while any_other_bidder == True:
    name_of_bidder = input("Enter name of the bidder: ")
    bid = int(input("Enter the bid amount: "))
    bidding[name_of_bidder] = bid
    ask = input("Is there any other bidder in the room: ")
    if ask == "no":
        any_other_bidder = False
        find_highest_bidder(bidding)
    elif ask == "yes":
        os.system('cls')
