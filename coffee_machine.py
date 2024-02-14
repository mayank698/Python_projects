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


def is_sufficient_resources(order_ingredients):
    """Returns true if order can be made otherwise returns false."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough resources.")
            return False
    return True


def process_coins():
    """Total calculated from coin inserted."""
    print("Please insert coin.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successfull(money_received, drink_cost):
    """Return true when the payment is accepted, of false when money is insufficient."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}₹ change.")
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")


is_on = True
while is_on:
    choice = input("Enter your desired drink: ").lower()
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ₹{profit}")

    else:
        drink = MENU[choice]
        if is_sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
