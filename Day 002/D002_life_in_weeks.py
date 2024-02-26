# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90, where 90 = 4000 weeks.

age = input("Enter your age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

weeks_left = ((90 - int(age)) *52)

print(f"You have {weeks_left} weeks left.")