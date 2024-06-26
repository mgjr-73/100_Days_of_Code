##############
# Challenge 1
##############
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Enter your guess letter: ")
guess = guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

# INSTRUCTOR CODE:
# word_list = ["aardvark", "baboon", "camel"]
#
# import random
# chosen_word = random.choice(word_list)
#
# guess = input("Guess a letter: ").lower()
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

##############
# Challenge 2
##############

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()
word_length = len(chosen_word)
display = []

for letter in range(word_length):
    display += "_"

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
guess = input("Enter your guess letter: ")
guess = guess.lower()

for index in range(word_length):
    if chosen_word[index] == guess:
        display[index] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

# INSTRUCTOR CODE:
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display += "_"
#
# guess = input("Guess a letter: ").lower()
#
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
#
# print(display)


##############
# Challenge 3
##############

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in chosen_word:
    guess = input("Enter your guess letter: ")
    guess = guess.lower()

    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess

    print (display)
    print("You win!")

# INSTRUCTOR SOLUTION:
# end_of_game = False
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     print(display)
#
#     #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")


##############
# Challenge 4
##############

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# TODO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."

while "_" in chosen_word:
    guess = input("Enter your guess letter: ")
    guess = guess.lower()

    if guess not in chosen_word:
        lives -= 1

    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess


# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
        break
    if lives == 0:
        print("You lose!")
        break

# INSTRUCTOR SOLUTION:
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

##########################
# Challenge 5 - Improve UI
##########################

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_wordlist
import hangman_art
word_list = hangman_wordlist.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])