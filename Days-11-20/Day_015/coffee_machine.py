import time
from data import MENU, resources
from os import system, name


# Coffee machine state. True = ON
power = True
money = 0


def clear_screen():
    """Clear the screen"""
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')

def format_order(order):
    if order == "e":
        return "espresso"
    elif order == "l":
        return "latte"
    elif order == "c":
        return "cappuccino"

def check_supplies(order):
    """
    Check if we have enough ingredients to fulfill order.\
    :return Dictionary
    """
    # Order ingredients
    water_needed = MENU[order]["ingredients"]["water"]
    milk_needed = MENU[order]["ingredients"]["milk"]
    coffee_needed = MENU[order]["ingredients"]["coffee"]

    # Check if we have enough ingredients to fulfill order
    if resources["water"] < water_needed or resources["milk"] < milk_needed or resources["coffee"] < coffee_needed:
        print(f'Sorry, we are low on ingredients and cannot make your "{order.capitalize()}"')
        print("Please notify the management to refill the machine. Sorry for the inconvenience.")
        time.sleep(5)
        clear_screen()
        print("Returning to main screen...")
        time.sleep(3)
        return [0, None]

    return [1, [water_needed, milk_needed, coffee_needed]]

def collect_money(customer_order, coffee_price, ingredients):
    deposited_coins = 0
    coin_types = {"quarters": .25, "dimes": .10, "nickels": .05, "pennies": .01}
    clear_screen()
    print("This machine only accepts coins.")
    time.sleep(3)

    payment_correct = False
    more_coins = True
    while more_coins:
        for coin in coin_types:
            clear_screen()
            print(f"Order: {customer_order.capitalize()}, Price: ${coffee_price:.2f}")
            print(f"Total coins deposited: ${deposited_coins:.2f}")
            insert_coin = input(f"How many {coin} ({coin_types[coin]})? ")
            if insert_coin == "":
                insert_coin = 0
            insert_coin = int(insert_coin)
            deposited_coins += insert_coin * coin_types[coin]

        if deposited_coins >= coffee_price:
            change = deposited_coins - coffee_price
            print(f"Your change is: ${change:.2f}")
            adjust_inventory(ingredients)
            time.sleep(2)
            payment_correct = True
            more_coins = False
        else:
            add_coins = input(f"{deposited_coins:.2f} is insufficient. Add more coins? (y/n) ")
            if add_coins == "n":
                print("Returning your coins.")
                time.sleep(2)
                more_coins = False

    return payment_correct

def adjust_inventory(ingredients):
    resources["water"] -= ingredients[0]
    resources["milk"] -= ingredients[1]
    resources["coffee"] -= ingredients[2]

def refill_machine():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100

def create_report():
    for bal in resources:
        print(f"{bal.capitalize()}: {resources[bal]}")
    print(f"Cash: ${money:.2f}")


while power:
    clear_screen()
    print("COFFEE MACHINE Model: CM-2024")
    customer_order = input("What would you like? (E)spresso/(L)atte/(C)appuccino): ")
    customer_order = customer_order.lower()

    if customer_order == "off":
        print("Shutting down...")
        time.sleep(3)
        break

    elif customer_order == "report":
        create_report()
        input("Press ENTER to return to main screen.")

    elif customer_order == "refill":
        clear_screen()
        print("Refilling machine...")
        time.sleep(3)
        refill_machine()
        create_report()
        print("Coffee machine ingredients replenished. Returning to main screen...")
        time.sleep(4)

    elif customer_order in ("e", "l", "c"):
        customer_order = format_order(customer_order)
        print(f'You are ordering "{customer_order.capitalize()}"')
        time.sleep(2)
        status, ingredients = check_supplies(customer_order)
        if status == 1:
            coffee_price = MENU[customer_order]["cost"]
            print(f"{customer_order} is {coffee_price}")
            if collect_money(customer_order, coffee_price, ingredients):
                money += coffee_price
                print(f"Making coffee now. Please wait.")
                time.sleep(3)
                print()
                print(f"Your {customer_order.capitalize()} is ready. Enjoy!")
                time.sleep(3)

    else:
        print("That is not a valid input.")
        time.sleep(2)














# TODO: Check transaction successful?
    # - Check that the user has inserted enough money to purchase the drink they selected
    # - if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and
    # this will be reflected the next time “report” is triggered.
    # - If the user has inserted too much money, the machine should offer change.

# TODO: Make Coffee
    # - If the transaction is successful and there are enough resources to make the drink the user selected, then the
    # ingredients to make the drink should be deducted from the coffee machine resources.
    # - Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of
    # drink.