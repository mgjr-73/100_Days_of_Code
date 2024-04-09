# ASCII art provided by instructor
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Player and computer throws
print("Let's play Rock, Paper, Scissors!")
print("1 = Rock, 2 = Paper, 3 = Scissors")
player_throw = int(input("Enter your choice (1, 2, or 3): "))

computer_throw = random.randint(1,3)

if player_throw == 1:
    print(f"Player: {rock}")
elif player_throw == 2:
    print(f"Player: {paper}")
else:
    print(f"Player: {scissors}")

if computer_throw == 1:
    print(f"Computer: {rock}")
elif computer_throw == 2:
    print(f"Computer: {paper}")
else:
    print(f"Computer: {scissors}")

# Throw evaluation
if player_throw == computer_throw:
    print("It's a draw!")
elif player_throw == 1 and computer_throw == 2:
    print("Computer wins!")
elif player_throw == 2 and computer_throw == 3:
    print("Computer wins!")
elif player_throw == 3 and computer_throw == 1:
    print("Computer wins")
else:
    print("Player wins!")

print("Thank you for playing")

