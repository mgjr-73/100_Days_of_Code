## Describe the Problem
Try to run a block of code then ask questions. For example, if you run this 
code, it will not print anything.
```python
def my_function():
    for i in range(1, 20)
        if i == 20:
            print("You got it")
my_function()   
```
- What is the for-loop doing?
  - *It is iterating through a range 1 through 20 but excluding 20*
- When is the function meant to print `"You got it!"`?
  - *When `i` equals `20`*
- What are your assumptions about `i`?
  - *The `range` function iterates from the first value up to, but not including the last value.*
  - *`i` will never reach `20`*
  - *To fix it, change the upper bound to `21`.*

## Reproduce the bug
```python
from random import randint

dice = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice[dice_num])
```
This code will produce an `IndexError: list index out of range`. To fix it, you need to 
change the lower limit from 1 to 0 and 6 to 5, since lists start at index 0, to cover all 6 items in the list 
(indexes 0, 1, 2, 3, 4, 5). Remember .

## Play Computer and Evaluate Each Line
```python
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
```
If input is 1994, the code will print nothing. To figure it out, evaluate the conditions whether True or False
- `year > 1980` = True
- `year < 1994` = False
- True and False = False
- `year > 1994` = False 
Therefore, input 1994 doesn't apply to any of the conditions. To fix it, the operand for `year < 1994` should be
`year <= 1994`.

## Fixing Errors and Watching for Red Underlines
```python
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
```
The obvious error is an indentation error and easy to fix.
```python
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
```
However, the code may still trigger a ValueError exception in case the user enters a string `twelve` instead of `12`.
The `int` method does not know how to parse a string, hence the exception raised. What you can do is copy the error 
and Google it.

Another error that might not be immediately obvious is the print string embedding the variable `age` enclosed in curly
brackets. To fix, use f-string method.

You can also use `try` method to customize the exception and also not break the execution.
```python
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
```
NOTE: The try method above is OK, but this is a script and it read from top to bottom. If we have
a mischievous user and still enters a string after raising the exception, we get the 
previous exception `ValueError: invalid literal for int() with base 10: 'twelve'` and the
program breaks.

## Squash bugs with a print() Statement
```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```
This code will print out 0.

To debug, you can try to print `word_per_page`. You will see that it is 0, which is true as this is the value assigned
to the variable in the first line. One would think that the value should change at the third line by the user input.
However, there is a difference between `=` which is a value assignment operator and `==` which is a comparison operator.
Whatever number the user enters, it just compares it to the 0 and evaluates to False. The equation basically comes out
to the value entered multiplied by 0 all the time. To fix this, use `=` to reassign a new value to `word_per_page`.

Also, the initializer (Line 1) can be removed since we can just directly assign whatever the user enters into the
`word_per_page` variable.

## Bringing out the BIG Gun: Using a Debugger
```python
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
```
Use a debugger to follow the steps by using breakpoints in pycharm.
- Step Over, executes code line-by-line.
- Step Into, will execute code line-by-line until it encounters an external module. Very useful for learning how
  a function works, whether it is built-in or written  by other people. 
- Step Out, Takes you out of Step Into, when you're done studying an external function and takes you back where you 
  left off before stepping in.
- Step Into My Code, does the same thing as Step Into but ignores built-in functions. To get out of your code, just use
  Step out.
- Also note the Threads & Variables and Console tabs.
- You can also click on the breakpoint icon or mute it to see
Solution:
```python
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
```
## Final Tips
- Take a break
- Ask a friend
- Run your code often
- Ask Stack Overflow

# Debugging Challenges

## Odd or Even
```python
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
```

Solution:
```python
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
```

## Leap Year
This is how you work out whether if a particular year is a leap year.
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder
```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```

Solution:
```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```

## Debugging FizzBuzz
The code needs to print the solution to the FizzBuzz game.
- Your program should print each number from 1 to x where x is the input number. 
- However when the number is divisible by 3 then instead of printing the number it should print "Fizz".   
- When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".
```python
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])
```

Solution:
```python
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
```