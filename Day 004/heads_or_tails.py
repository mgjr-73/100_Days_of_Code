'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number,
either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails
'''

import random

# Using random.randint
side = random.randint(0, 1)
if side == 0:
    print("Tails")
else:
    print("Heads")

# Using random.choice. Ref: https://stackoverflow.com/questions/306400/how-can-i-randomly-select-choose-an-item-from-a-list-get-a-random-element
sides = ["Heads", "Tails"]
print(random.choice(sides))