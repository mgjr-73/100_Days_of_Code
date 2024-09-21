# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # - Check the user’s input to decide what to do next.
    # - The prompt should show every time action has completed

# TODO: Turn off the Coffee Machine by entering “off”to the prompt.
    # code should end execution

# TODO: Print report.
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource
    # values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5

# TODO: Check resources sufficient?
    # - When the user chooses a drink, the program should check if there are enough resources to make that drink.
    # - If not enough resources, print “Sorry there is not enough <resource type>.”

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