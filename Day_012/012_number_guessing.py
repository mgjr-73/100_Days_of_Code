#Number Guessing Game Objectives:

# Include an ASCII art logo.
import ascii_logo
import random

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def guesses():
    difficulty = input("Pick a level. Type 'e' for easy' or 'h' for hard: ")
    if difficulty == "e":
        return 10
    else:
        return 5

def number():
    answer = random.randint(1, 100)
    return answer

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
def compare_guess(correct_answer, guess):
    if guess < correct_answer:
        print("Too low!")
    elif guess > correct_answer:
        print("Too high!")
    else:
        print(f"The correct answer is: {correct_answer}")
        print("You got it!")
        exit(0)


print(ascii_logo.logo)
print()
print(f"I'm thinking of a number between 1 and 100.")
answer = number()
# Track the number of turns remaining.
level = guesses()
while level > 0:
# Allow the player to submit a guess for a number between 1 and 100.
    print(f"You have {level} guesses left.")
    player_guess = int(input("Make a guess: "))
    compare_guess(answer, player_guess)
    level = level - 1

# If they run out of turns, provide feedback to the player.
print("Sorry you ran out of guesses")
print(f"The correct answer is {answer}.")
exit(0)
