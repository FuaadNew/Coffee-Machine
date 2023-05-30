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


def resourcesufficient(ingredients):

    for item in ingredients:
        if ingredients[item] >resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def sucessfultransaction(money,cost):

    if money >= cost:
        change = round(money - cost,2)
        print (f"Here is ${change} in change.")
        global profit
        profit+=cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False




def make_coffee(drink,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}☕. Enjoy!")



is_on = True

while is_on:
    Decision = input("What would you like? (espresso/latte/cappuccino) ")
    if Decision == "off":
        is_on = False
    elif Decision == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[Decision]
        if resourcesufficient(drink["ingredients"]):
            payment = process_coins()
            if sucessfultransaction(payment, drink["cost"]):
                make_coffee(Decision, drink["ingredients"])





















