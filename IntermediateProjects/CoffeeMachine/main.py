
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
order_possible = True

def get_report():
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: {money}")

def money_inserted():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters/4) + (dimes/10) + (nickles/20) + (pennies/100)
    money = total
    return money

def check_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def update_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount


while order_possible:

    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    def check_prompt(prompt):
        global order_possible
        if prompt == "report":
            get_report()
        elif prompt in MENU:
            if check_resources(prompt):
                money_received = money_inserted()
                cost = MENU[prompt]["cost"]
                if money_received >= cost:
                    change = round(money_received - cost, 2)
                    print(f"Here is ${change} in change.\nHere is your {prompt}. Enjoy!")
                    update_resources(prompt)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                order_possible = False
        else:
            print("Invalid choice! Please try again.")

    check_prompt(prompt)
