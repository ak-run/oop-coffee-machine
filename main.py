from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if drink != None and coffee_machine.is_resource_sufficient(drink):
            cost = drink.cost
            money_machine.make_payment(cost)
            coffee_machine.make_coffee(drink)
