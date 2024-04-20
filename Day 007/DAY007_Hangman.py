import random
import hangman_wordlist
import hangman_art
from os import system, name

end_of_game = False
lives = 6

word_list = hangman_wordlist.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed = []
display = []

print(hangman_art.logo)
print(f"The mystery word has {word_length} letters.")

for letter in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Enter your guess letter: ").lower()

    # Refresh screen before printing result. See https://www.geeksforgeeks.org/clear-screen-python/
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')

    if guess in guessed:
        print(f'You already used "{guess}".')
    elif guess in chosen_word:
        print(f"Yes, there's '{guess}' in the mystery word!")
    elif guess not in chosen_word:
        print(f"Oops. There's no '{guess}' in the mystery word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'You lose! The mystery word is: "{chosen_word}"')

    guessed += guess

    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    # Check if there are no more "_" in 'display'
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")
    print()

print("Thank you for playing.")


###############################
# Instructor Code
###############################
# import random
#
# # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# # Delete this line: word_list = ["ardvark", "baboon", "camel"]
# from hangman_words import word_list
#
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# end_of_game = False
# lives = 6
#
# # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo
#
# print(logo)
#
# # Testing code
# # print(f'Pssst, the solution is {chosen_word}.')
#
# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")
#
#     # Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     # Check if user is wrong.
#     if guess not in chosen_word:
#         # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     # Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     # Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     # TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from hangman_art import stages
#
#     print(stages[lives])