
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

#TODO: Add a function that returns the cost of a beverage

is_on = True

def check_resources(beverage):
    """checks if there is enough resources to make the beverage"""
    for item in beverage["ingredients"]:
        if beverage["ingredients"][item ] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def check_price(beverage):
   """returns the total calculated from coin inserted"""
   print(f"The {beverage} costs ${beverage['cost']}")
   print("Please insert coin")
   total = int(input("How many quarters? ")) * 0.25
   total += int(input("How many dimes? ")) * 0.1
   total += int(input("How many nickles? ")) * 0.05
   total += int(input("How many pennies? ")) * 0.01 
   return total

def check_money(money_received, drink_cost):
    """checks if the user has enough money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        global profit
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
while is_on:
    """main program"""
    Choice = input(print("What would you like? (espresso/latte/cappuccino): "))  
    if Choice == "off":
        is_on = False
        print("Machine is off.")
    elif Choice == "report":
        print(f"{resources} profit = {profit}")
    else:
        drink = MENU[Choice]
        if check_resources(drink):
            payment = check_price(drink)
            if check_money(payment, drink["cost"]):
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]

            
                

    


