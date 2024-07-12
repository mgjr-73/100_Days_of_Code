# This is Day 11 of 100 Days of Code where we complete a capstone project, a Blackjack game.
# My plan:
# ========
# Step 1. Determine dealer hand. Dealer will keep second card hidden until Step 4.
# Step 2. Determine player hand
# Step 3. Does either player need to hit?
# Step 4. Compare dealer and player hands and announce who wins or loses or if it is a draw.
# Step 5. Ask to play again or exit the program.

import random
from os import system, name


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    """Emulate the 'clear screen' command based on the current OS"""
    if name == 'nt':   # for Windows
        _ = system('cls')
    else:   # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

def draw_cards(num_cards=2):
    """Draw random card from cards list and return a list"""
    extra_cards = []
    for draw in range(num_cards):
        card = random.choice(cards)
        extra_cards.append(card)
    return extra_cards

def get_hand():
    """Dealer automatically draws additional cards as long as sum of cards <17."""
    hand = draw_cards()
    return hand

def get_hand_total(issued_cards):
    """Evaluate presence of 11 cards, make necessary adjustments then get sum total of cards"""
    total = 0
    for card in issued_cards:
        total += card
    if 11 in issued_cards and total > 21:
        return total-10

    return total

def check_blackjack():
    pass

def player_bust():
    clear()
    print(f"Dealer: {dealer}, Total: {dealer_total}")
    print()
    print(f"Player: {player}, Total: {player_total}")
    print()
    print("Player BUST! Dealer wins!")
    play_again()

def dealer_bust():
    clear()
    print(f"Dealer: {dealer}, Total: {dealer_total}")
    print()
    print(f"Player: {player}, Total: {player_total}")
    print()
    print("Dealer BUST! Player wins!")
    play_again()

def evaluate_winner():
    clear()
    print(f"Dealer: {dealer}, Total: {dealer_total}")
    print()
    print(f"Player: {player}, Total: {player_total}")
    if dealer_total > 21:
        dealer_bust()
    elif dealer_total > player_total:
        print()
        print("Dealer wins!")
        play_again()
    elif dealer_total == player_total:
        print()
        print("It's a draw!")
        play_again()
    else:
        print()
        print("Player wins!")
        play_again()


def play_again():
    again = input("Do you want to play again? (y/n): ")
    if again == "n":
        exit(0)


while True:
    clear()
    # Player and Dealer round 1: Dealer Shows only one card, Player shows full hand.
    dealer = get_hand()
    dealer_total = get_hand_total(dealer)
    if dealer_total == 21:
        clear()
        print(dealer)
        print("Dealer has Blackjack. Dealer Wins!")
        play_again()
    else:
        dealer_hand1 = f"Dealer hand: [{dealer[0]}, X]"
        print(dealer_hand1)
        print()

    player = get_hand()
    player_total = get_hand_total(player)
    if player_total == 21 and dealer_total == 21:
        clear()
        print(f"Dealer hand: {dealer}, Total: {dealer_total}")
        print()
        print(f" Player hand: {player}, Total: {player_total}")
        print()
        print("Both Dealer and Player got Blackjack. Dealer WINS!")
        play_again()
    elif player_total == 21 and dealer_total != 21:
        clear()
        print(dealer)
        print()
        print(player)
        print("Player has Blackjack. Player WINS!")
        play_again()
    else:
        print(f"Player hand: {player}, Total: {player_total}")

    # Player and dealer round 2: Player hit or stay. Dealer keeps hitting while total <17
    keep_hitting = True
    while keep_hitting:
        hit = input("Player: Type 'h' to Hit, or 's' to Stay: ").lower()
        clear()
        if hit == "s":
            if dealer_total > player_total:
                evaluate_winner()
            else:
                keep_hitting = False
        else:
            player += draw_cards(1)
            player_total = get_hand_total(player)
            if player_total > 21:
                player_bust()
            else:
                print(dealer_hand1)
                print()
                print(f"Player hand: {player}, Total: {player_total}")

    # Evaluate dealer hand
    dealer_total = get_hand_total(dealer)
    while dealer_total < 17:
        dealer += draw_cards(1)
        print(dealer)
        dealer_total = get_hand_total(dealer)

    # Evaluate winner
    clear()
    evaluate_winner()


