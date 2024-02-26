#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line.
# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Hello and welcome to the band name generator!")  #1
city = input("What's the name of the city you grew up in?\n> ")  #2
pet_name = input("What's a good name for a pet?\n> ")  #3

print('Your band name is "' + city.title() + ' ' + pet_name + '"!')  #4 Notice application of title() method.

# Another way to write #4 is to use .format(), where positional arguments are passed into the curly braces.
print('Your band name is "{} {}"!'.format(city, pet_name).title())

# Yet another way to write it is to use f-string.
print(f'Your band name is "{city} {pet_name}"!')
