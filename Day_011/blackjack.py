# This is Day 11 of 100 Days of Code where we complete a capstone project, a Blackjack game.
# My plan:
# ========
# Step 1. Determine dealer hand. Dealer will keep second card hidden until Step 4.
# Step 2. Determine player hand
# Step 3. Does either player need to hit?
# Step 4. Compare dealer and player hands and announce who wins or loses or if it is a draw.
# Step 5. Ask to play again or exit the program.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(num_cards=2):
    """Draw random card from cards list and return a list"""
    hand = []
    for draw in range(num_cards):
        card = random.choice(cards)
        hand.append(card)
    return hand

def get_dealer_hand():
    """
    Dealer automatically draws additional cards as long as sum of cards <17.
    """
    dealer_hand = draw_cards()
    dealer_total = add_cards(dealer_hand)
    # Dealer hit
    while dealer_total < 17:
        dealer_hand += draw_cards(1)
        dealer_total = add_cards(dealer_hand)
        continue
    print(f"Dealer total: {dealer_total}")  # Delete this line at final
    return dealer_hand

def get_player_hand():
    """Draw two cards for player"""
    player_hand = draw_cards()
    return player_hand

def player_hit():
    print("You got another card!")

def add_cards(issued_cards):
    """Get sum total of cards"""
    total = 0
    for card in issued_cards:
        total += card
    return total


# Dealer round 1: Show only one card.
dealer = get_dealer_hand()
print(dealer)    # Delete this line at final.
print(f"Dealer hand: [{dealer[0]}, X]")
print()

# Player round1: Show first two cards and total.
player = get_player_hand()
player_total = add_cards(player)
print(f"Player hand: {player}")
print(f"Player Total: {player_total}")

# Ask player to hit
hit = input("Type 'h' to Hit, or 's' to Stay: ").lower()
if hit == "h":
    player_hit()
else:
    pass
