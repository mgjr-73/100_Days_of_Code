print("Welcome to the rollercoaster ride!")
tier3_tix = 14
tier2_tix = 10
tier1_tix = 7
bill = 0
height = int(input("What is your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill += tier1_tix
        print(f"Your ticket price is ${bill}.")
    elif age < 18:
        bill += tier2_tix
        print(f"Your ticket price is ${bill}.")
    elif age < 45:
        bill += tier3_tix
        print(f"Your ticket price is ${bill}")
    elif age == 45 or age <= 55:
        print(f"Your ticket price is ${bill}")

    add_photo = input("Do you want add a photo for $3 (y/n)? ")
    if add_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the rollercoaster.")