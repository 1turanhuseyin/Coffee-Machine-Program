from data import MENU, resources
from art import logo

espresso_water_amount = MENU["espresso"]["ingredients"]["water"]
espresso_coffee_amount = MENU["espresso"]["ingredients"]["coffee"]

latte_water_amount = MENU["latte"]["ingredients"]["water"]
latte_milk_amount = MENU["latte"]["ingredients"]["milk"]
latte_coffee_amount = MENU["latte"]["ingredients"]["coffee"]

cappuccino_water_amount = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk_amount = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee_amount = MENU["cappuccino"]["ingredients"]["coffee"]


def update_resources(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]


def check_resources(coffee_type):
    is_enough = True
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        if is_enough:
            print()
        print(f"Sorry there is not enough water for {coffee_type}.")
        is_enough = False

    if coffee_type != "espresso" and resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        if is_enough:
            print()
        print(f"Sorry there is not enough milk for {coffee_type}.")
        is_enough = False

    if resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        if is_enough:
            print()
        print(f"Sorry there is not enough coffee for {coffee_type}.")
        is_enough = False

    return is_enough

is_machine_on = True
money = 0

while is_machine_on:
    print(logo)
    coffee = input("What would you like?:\t").lower()
    input_list = ["espresso", "latte", "cappuccino", "off", "report"]

    while not coffee in input_list:
        print("You entered a wrong value! Please enter an exist value.\n")
        print(logo)
        coffee = input("What would you like?:\t").lower()

    if coffee == "off":
        is_machine_on = False
    elif coffee == "report":
        print(f"\n\tWater: {resources["water"]}ml\n\tMilk: {resources["milk"]}ml\n\tCoffee: {resources["coffee"]}g\n\tMoney: ${money}\n")
    else:
        if not check_resources(coffee):
            print("Please try again.\n")
        else:
            print("\nPlease insert coins.")
            quarters = int(input("How many quarters?($0.25):\t"))
            dimes = int(input("How many dimes?($0.10):\t"))
            nickles = int(input("How many nickles?($0.05):\t"))
            pennies = int(input("How many pennies?($0.01):\t"))
            print()

            total_coins = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
            coffee_cost = MENU[coffee]["cost"]

            if total_coins < coffee_cost:
                print(f"Sorry that's not enough money for {coffee}. Money(${round(total_coins, 2)}) refunded.\n")
            else:
                money += coffee_cost
                change = total_coins - coffee_cost

                update_resources(coffee)

                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")

                print(f"Here is your {coffee}☕️ Enjoy!\n")



print("Good bye☕")
