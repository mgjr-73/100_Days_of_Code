from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino/): ”
#    a. Check the user’s input to decide what to do next.
#    b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
#       The prompt should show again to serve the next customer.

# 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
#    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
#       Your code should end execution when this happens.
power_on = True

while power_on:
    choices = menu.get_items()
    choice = input(f"What would you like? {choices}: ")
    if choice == "off":
        power_on = False

    # 3. Print report.
    #    a. When the user enters “report” to the prompt, a report should be generated that shows the current resource
    #       values.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    # 4. Check resources sufficient?
    #    a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    #    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make
    #       the drink but print: “ Sorry there is not enough water.”
    #    c. The same should happen if another resource is depleted, e.g. milk or coffee.
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            # 5.Process coins.
            #   a. If there are sufficient resources to make the drink selected, then the program should prompt the user to
            #      insert coins.
            # 6. Check transaction successful?
            #    a. Check that the user has inserted enough money to purchase the drink they selected.
            #    b. But if the user has inserted enough money, then the cost of the drink gets added to the
            #       machine as the profit and this will be reflected the next time “report” is triggered.
            #    c. If the user has inserted too much money, the machine should offer change.
            if money_machine.make_payment(order.cost):
                # 7. Make Coffee.
                #    a. If the transaction is successful and there are enough resources to make the drink the user
                #       selected, then the ingredients to make the drink should be deducted from the coffee machine
                #       resources.
                coffee_maker.make_coffee(order)

