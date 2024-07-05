import art
from os import system, name


def clear():
    if name == 'nt':   # for Windows
        _ = system('cls')
    else:   # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

def highest_bidder():
    pass


print(art.logo)
print("Welcome to the secret auction program.")

add_bidder = True
bids = {}

while add_bidder:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    other_bidder = input("Are there any other bidders? (Type 'yes' or 'no'): ")

    # Add bidder information to dictionary
    pass

    if other_bidder == "no":
        add_bidder = False
    else:
        clear()
        pass

highest_bidder()
clear()
print("The winning bid is...")




#################
# Instructor Code
#################
# from replit import clear
#
# from art import logo
#
# print(logo)
#
# bids = {}
# bidding_finished = False
#
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     # bidding_record = {"Angela": 123, "James": 321}
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#
# while not bidding_finished:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         clear()
#
# """
# FAQ: My console doesn't clear()
#
# This will happen if you’re using an IDE other than replit.
# I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so:
#
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076
#
# """