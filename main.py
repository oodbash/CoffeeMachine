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

special_commands = ["off","report"]
end_of_main = None

def report():
    print(f"\nWater -> {resources['water']}\nMilk --> {resources['milk']}\nCoffee > {resources['coffee']}")

def choose_from_menu():
    good_choice = False
    while good_choice == False:
        print("\nWhat would you like from menu?\n")
        menu_options = []
        for i in MENU:
            print(i)
            menu_options.append(i)
            menu_options.extend(special_commands)
        choice = (input("\nYour choice is: ")).lower()
        if choice in special_commands:
            print(f"\nSir, yes Sir.. {choice}")
            good_choice = True
        elif choice not in menu_options:
            print("\nYou need to chose something from the menu. Please try again..\n")
        else:
            print(f"\nGood choice, {choice} it is!")
            good_choice = True
    return choice

def main():
    end_of_main = False
    while end_of_main != True:
        my_choice = choose_from_menu()
        if my_choice == "off":
            end_of_main = True
            print("\nBye, bye..")
        if my_choice == "report":
            report()
        


main()
