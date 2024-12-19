
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

water_report = resources["water"]
milk_report = resources["milk"]
coffee_report = resources["coffee"]
money = 0
change = 0


def get_report():
    print(f"Water: {water_report} \nMilk: {milk_report} \nCoffee: {coffee_report} \nMoney: {money}")

def money_inserted():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters/4) + (dimes/10) + (nickles/20) + (pennies/100)
    money = total
    return money

prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

def check_prompt(prompt):
    if prompt == "report":
        print("testing report")
        get_report()
    
    money = money_inserted()
    if prompt == "espresso":
        cost = MENU["espresso"]["cost"]
        if money > cost:
            change = money - cost
            print(f"Here is ${change} in change.\nHere is your {prompt} Enjoy!")
    elif prompt == "latte":
        cost = MENU["latte"]["cost"]
        if money > cost:
            change = money - cost
            print(f"money inserted is: {money} and cost is: {cost} and change is {change}")
    elif prompt == "cappucino":
        cost = MENU["cappucino"]["cost"]
        if money > cost:
            change = money - cost
            print(f"money inserted is: {money} and cost is: {cost} and change is {change}")


check_prompt(prompt)
