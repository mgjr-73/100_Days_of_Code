import time
from data import MENU, resources
from os import system, name


# Coffee machine state. True = ON
power = True

# Ingredients
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

# Cash in machine
money = 0


def clear_screen():
    """Clear the screen"""
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')

def process_order(order):
    """Send order to appropriate function"""
    result = ""
    if order == "e":
        print("espresso!")
    if order == "l":
        print("latte!")
    if order == "c":
        print("cappuccino!")
    if order == "report":
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: {money}")

    return result

# TODO: Check resources sufficient?
    # - When the user chooses a drink, the program should check if there are enough resources to make that drink.
    # - If not enough resources, print “Sorry there is not enough <resource type>.”
def check_resources():
    pass


while power:
    clear_screen()
    customer_order = input("What would you like? (e)spresso/(l)atte/(c)appuccino): ")
    if customer_order != "off":
        process_order(customer_order)
        print()
        input("Order processed. Press ENTER to continue.")
    else:
        print("Shutting down...")
        time.sleep(3)
        power = False









# TODO: Process coins
    # - If there are sufficient resources to make the drink selected, then the program should prompt the user to
    # insert coins.
    # - Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies =
    # 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

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