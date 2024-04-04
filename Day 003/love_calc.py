import time

'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
'''
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  # What is your name?
name2 = input("What is your partner's name? ")  # What is their name?

names = (name1 + name2)
# Remove all spaces. First, .strip() ensures that leading and trailing spaces, if any, are removed. .replace(" ", "")
# replaces white space " " with no space "".
names = names.lower().strip().replace(" ","")

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
l = names.count('l')
o = names.count('o')
v = names.count('v')
e2 = names.count('e')
total1 = t+r+u+e
total2 = l+o+v+e
total = total1 * 10 + total2

# print(f"T occurs {t} times")
# print(f"R occurs {r} times")
# print(f"U occurs {u} times")
# print(f"E occurs {e} times")
# print(f"Total = {total1}")
# print()
# print(f"L occurs {l} times")
# print(f"O occurs {o} times")
# print(f"V occurs {v} times")
# print(f"E occurs {e} times")
# print(f"Total = {total2}")

print()
print("The love calculator is calculating your score...")
time.sleep(3)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

#==========================
# Instructor Solution
#==========================

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')
# first_digit = t+r+u+e
#
# l = names.count('l')
# o = names.count('o')
# v = names.count('v')
# e = names.count('e')
# second_digit = l+o+v+e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
