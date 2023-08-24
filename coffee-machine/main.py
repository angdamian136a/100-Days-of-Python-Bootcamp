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

water_cfm = resources["water"]
milk_cfm = resources["milk"]
coffee_cfm = resources["coffee"]
money_cfm = 0
machine_on = True

while machine_on == True:
    # TODO: 1. Prompt the user, query on what coffee.
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    # Prompt should show every time an action is complete (once the drink is dispensed) to serve the next customer

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt
    if coffee_choice == "off":
        machine_on = False
        break

    # TODO: 3. Print report
    elif coffee_choice == "report":
        print(f"Water: {water_cfm}ml "
              f"\nMilk: {milk_cfm}ml "
              f"\nCoffee: {coffee_cfm}g "
              f"\nMoney: ${money_cfm}")
        continue

    # TODO: 4. Check whether resources are sufficient
    else:
        water_needed = MENU[coffee_choice]["ingredients"]["water"]
        milk_needed = 0
        if coffee_choice != "espresso":
            milk_needed = MENU[coffee_choice]["ingredients"]["milk"]
        coffee_needed = MENU[coffee_choice]["ingredients"]["coffee"]
        money_needed = MENU[coffee_choice]["cost"]
        print(water_needed)
        print(milk_needed)
        print(coffee_needed)
        print(money_needed)
        if water_needed > water_cfm:
            print("Sorry, there is not enough water.")
            continue
        elif milk_needed > milk_cfm:
            print("Sorry, there is not enough milk.")
            continue
        elif coffee_needed > coffee_cfm:
            print("Sorry, there is not enough coffee.")
            continue
        # TODO: 5. Process coins. If resources are sufficient, prompt payment.
        else:
            print(f"Please pay ${money_needed}.")
            num_quarters = int(input("How many quarters?:"))
            num_dimes = int(input("How many dimes?:"))
            num_nickles = int(input("How many nickles?:"))
            num_pennies = int(input("How many pennies?:"))
            money_received = num_quarters*0.25 + num_dimes*0.10 + num_nickles*0.05 + num_pennies*0.01
            # TODO: 6. Check transaction successful. Has the user inserted enough money?
            if money_received < money_needed:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                # TODO: 7. Make the coffee. Deduct resources and collect money in the coffee machine
                money_refund = money_received - money_needed
                money_refund = round(money_refund, 2)
                money_cfm += money_needed
                water_cfm -= water_needed
                milk_cfm -= milk_needed
                coffee_cfm -= coffee_needed
                print(f"Here is ${money_refund} change.")
                print(f"Here is your {coffee_choice}. Enjoy!")
            continue





