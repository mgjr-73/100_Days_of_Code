"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

From https://www.vedantu.com/maths/how-to-find-prime-numbers
Numbers <= 40 ... 6n + 1 or 6n -1
Number > 40 ... n^2 + n + 41

Points to be Noted
Numbers having even numbers in one’ place cannot be a prime number.

Only 2 is an even prime number; all the rest prime numbers are odd numbers.

To find whether a larger number is prime or not, add all the digits in a number, if the sum is divisible by 3 it is not a prime number.

Except 2 and 3, all the other prime numbers can be expressed in the general form as    6n + 1 or 6n - 1, where n is the natural number.
"""

def prime_checker(number):
    x = number % 2
    y = number % 4
    z = number % 3

    if number in range(1, 4):
        print("It's a prime number.")
    elif x == 0 or y == 0 or z == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Enter a number from 0 to 100: "))
prime_checker(number=n)

###################
# Instructor's Code
###################
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
