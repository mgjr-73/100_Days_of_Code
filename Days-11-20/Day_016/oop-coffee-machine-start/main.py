from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True

while on:
    menu_items = menu.get_items()
    customer_choice = input(f"What would you like? ({menu_items}): ")
    if customer_choice == "off":
        on = False
    elif customer_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
       drink = menu.find_drink(customer_choice)

       if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)

