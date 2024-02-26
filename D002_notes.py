#Data Types

#String
"Hello"
print("Hello"[0]) # will print 'H'  # The method of pulling out an element from a string is called 'subscripting'.


#Integer
123
123_456_999 # This is still integers. Python will ignore underscores.

#Float
3.14159

#Boolean
True
False

#Type Errors
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")

#Type Checking
type()

#Type Conversion
str()
int()
float()
bool()

# Maths Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

#Rounding Numbers
print(round(4.6666666666)) # result 5
print(round(4.6666666666, 2))   # result 4.67

#Floor division
9 // 4  # chops off float without rounding, returns 'int' type instead of 'float'. Result is 2.

#Shorthand Operators
# a += 2  short for a = a + 2
# -=
# *=
# /=


#f-Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")