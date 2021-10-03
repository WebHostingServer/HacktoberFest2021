# In need of coffee but it's lockdown,
# so Here I bring a digital coffee machine...


import os
import coffeeMachine_art
from coffeeMachine_data import MENU, resources

money_in_machine = 0
machine_ON = True


def make_transaction():
    print("Please insert coins.")
    money = float(input("how many quarters($0.25)?: ")) * 0.25
    money += float(input("how many dimes($0.10)?: ")) * 0.10
    money += float(input("how many nickles($0.05)?: ")) * 0.05
    money += float(input("how many pennies($0.01)?: ")) * 0.01
    return money


def resources_check(key):
    if resources['water'] < MENU[key]['ingredients']['water']:
        print(f"Sorry there is not enough water.")
        return False
    elif resources['coffee'] < MENU[key]['ingredients']['coffee']:
        print(f"Sorry there is not enough coffee.")
        return False
    elif key != 'espresso' and resources['milk'] < MENU[key]['ingredients']['milk']:
        print(f"Sorry there is not enough water.")
        return False
    else:
        resources['water'] -= MENU[key]['ingredients']['water']
        resources['coffee'] -= MENU[key]['ingredients']['coffee']
        if key != 'espresso':
            resources['milk'] -= MENU[key]['ingredients']['milk']
        return True


def make_coffee(key):
    global money_in_machine
    money_required = MENU[key]["cost"]
    if resources_check(key):
        print(f"Cost: ${MENU[key]['cost']}")
        money_received = make_transaction()
        if money_received < money_required:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money_in_machine += money_required
            money_return = round(money_received - money_required, 2)
            print(f"Here is ${money_return} change.")
            print(f"Here is your {key} ☕. Enjoy!")


os.system('clear')
print(coffeeMachine_art.coffee_art)
print(coffeeMachine_art.logo)

while machine_ON:
    print('''
    What would you like?
    1. 'Espresso'
    2. 'Latte'
    3. 'Cappuccino'
    4. 'Report' (for knowing current status of resources in the machine)
    5. 'Off' (for turning off the machine)
    ''')
    choice = input("Type your desired option: ").lower()

    if choice == 'off':
        machine_ON = False
        print("Thank you for using coffee machine...")
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${money_in_machine}")
        input("Press Enter to continue...")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        make_coffee(choice)
        input("Press Enter to continue...")
    else:
        print("Invalid choice...")
        input("Press Enter to continue...")