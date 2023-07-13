from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    # asking user to choose a drink
    choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    # actions based on answer
    # turns machine off
    if choice == "off":
        is_on = False
    # prints report
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        # if drink on the menu and resource sufficient machine asks for payment
        if drink is not None and coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                # if payment successful makes a drink
                coffee_machine.make_coffee(drink)
    # if choice not on the menu, user is prompted for input again

