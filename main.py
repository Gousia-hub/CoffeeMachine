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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sry! There is not enough {item}")
            return False
    return True


def coins():
    """"Returns total calculated from user coins"""
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def transaction_successful(order_cost, total):
    """"Checks the money sufficient to make coffee or not and returns accordingly"""
    if total < order_cost:
        print("Not enough money! money refunded")
        return False
    else:
        print("ur coffee ☕ is ready")
        print(f"Here is ${round(total-order_cost, 2)} in change")
        global profit
        profit += order_cost
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    # secret code to off the machine
    if choice == "off":
        is_on = False
    elif choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"water: {water}ml \n milk: {milk}ml \n coffee: {coffee}g \n money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            print("Insert the coins")
            quarters = int(input("How many quarters ?"))
            dimes = int(input("How many dimes ?"))
            nickles = int(input("How many nickles ?"))
            pennies = int(input("How many pennies ?"))
            transaction_successful(drink["cost"], total=coins())
            make_coffee(choice, drink["ingredients"])
