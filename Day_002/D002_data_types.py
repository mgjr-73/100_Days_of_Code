two_digit_number = input("Enter numbers:  ")
# 🚨 Don't change the code above 👆
####################################
# 'input' function returns type 'str'. For this problem, each digit of the input must be added
# so that "39" results in 12.
# Write your code below this line 👇
y = 0
for x in range(len(two_digit_number)):
    y += int(two_digit_number[x])
print(y)

