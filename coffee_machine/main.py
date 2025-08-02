from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffe_menu = Menu()


is_on = True
while is_on:
    options = coffe_menu.get_items()
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_money_machine.report()
        coffee_maker.report()
    else:
        drink = coffe_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and coffee_money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
