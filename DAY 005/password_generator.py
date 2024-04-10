#Password Generator Project
# Begin instructor provided code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# End instructor provided code

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pw_letters = []
# pw_numbers = []
# pw_symbols = []
# for l in range(1, nr_letters + 1):
#     letter_index = random.randint(0, (len(letters)-1))
#     pw_letters += (letters[letter_index])
#
# for s in range(1, nr_symbols + 1):
#     symbol_index = random.randint(0, (len(symbols)-1))
#     pw_symbols += (symbols[symbol_index])
#
# for n in range(1, nr_numbers + 1):
#     number_index = random.randint(0, (len(numbers)-1))
#     pw_numbers += (numbers[number_index])
#
# pw_set = pw_letters + pw_symbols + pw_numbers
#
# for pw in range(len(pw_set)):
#     print(pw_set[pw], end='')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pw_letters = []
pw_numbers = []
pw_symbols = []
for l in range(1, nr_letters + 1):
    letter_index = random.randint(0, (len(letters)-1))
    pw_letters += (letters[letter_index])

for s in range(1, nr_symbols + 1):
    symbol_index = random.randint(0, (len(symbols)-1))
    pw_symbols += (symbols[symbol_index])

for n in range(1, nr_numbers + 1):
    number_index = random.randint(0, (len(numbers)-1))
    pw_numbers += (numbers[number_index])

pw_set = pw_letters + pw_symbols + pw_numbers
random.shuffle(pw_set)  # Randomize list. Ref: https://www.w3schools.com/python/ref_random_shuffle.asp

print("Your password is:")
for pw in range(len(pw_set)):
    print(pw_set[pw], end='')

# See password_generator_instructor.py to compare instructor's solution.
