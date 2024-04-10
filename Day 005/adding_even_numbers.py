"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
"""
print("Enter a number between 0 and 1000.")
# Begin instructor code
target = int(input("> "))  # Enter a number between 0 and 1000
# End instructor code
if target > 1000:
    print("That is above 1000!")
else:
    total = 0
    if target % 2 == 0:
        for n in range (2, target + 1, 2):
            total += n
    else:
        for n in range(2, target, 2):
            total += n

    print(total)


######################
# Instructor Solution
######################
# even_sum = 0
# for number in range(2, target + 1, 2):
#   even_sum += number
# print(even_sum)
#
# # or
#
# # alternative_sum = 0
# # for number in range(1, target + 1):
# #   if number % 2 == 0:
# #     alternative_sum += number
# # print(alternative_sum)