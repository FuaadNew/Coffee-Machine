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
profit = 0

def is_resource_sufficient(order_ingredients):
    for resource in resources:
        if order_ingredients[resource] > resources[resource]:
            print( f"Sorry there is not enough {resource}.")
            return False
        else:
            return True


def process_coins(cost):
    global profit
    total =0
    print("Please insert coins.")
    total += int(input("how many quarters?:")) *.25
    total += int(input("how many dimes?:")) * .10
    total += int(input("how many nickles?:")) * .05
    total += int(input("how many pennies?:")) * .01
    if total > cost:
        change = round(total-cost,2)
        print(f"Here is your change.${change}")
        profit+=cost
    elif total ==cost:
        profit+=cost

    else:
      print("Sorry that's not enough money. Money refunded.")




def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item]-= drink_ingredients[item]
    print("Here is your latte. Enjoy!")











on= True
while on:
    choice = input("“What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        on= False
    elif choice == "report":
        for item in resources:
            if item !="coffee":
                print(f"{item}: {resources[item]}ml")
            else:
                print(f"{item}: {resources[item]}g\nMoney: ${profit}")
    else:
        drink = MENU[choice]
        cost = MENU[choice]["cost"]
        if is_resource_sufficient(drink["ingredients"]):
            process_coins(cost)
            make_coffee(drink["ingredients"])




















