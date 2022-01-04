MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "deset":10,
    "pedeset":50,
    "sto":100,
    "petsto":500
}

special_commands = ["off","report"]
end_of_main = None

def report():
    print(f"\nWater -> {resources['water']}\nMilk --> {resources['milk']}\nCoffee > {resources['coffee']}")

def check_resources(coffe):
    enough_resources = True
    missing_resources = []
    for i in MENU[coffe]['ingredients']:
        if MENU[coffe]['ingredients'][i] > resources[i]:
            enough_resources = False
            print(f"Sorry there is not enough {i}.")
    if enough_resources == True:
        print("We are ready to brew some coffe :)")
        return True
    else:
        return False

def get_money(coffe):
    total_amount = 0
    coffe_price = int(MENU[coffe]['cost'])
    enough = False
    print(f"Price of your coffe is {coffe_price}")
    print("Please put the money in the machine: ")
    while enough == False:
        for m in money:
            nom = input(f"{money[m]}x")
            if nom.isnumeric():
                total_amount += int(money[m])*int(nom)
            elif nom == "":
                total_amount += 0
            else:
                print("We cannot accept this :(")
        print(f"Total amount of money that you provided is {total_amount}")
        if total_amount >= coffe_price:
            print("You have enough money. You will get your coffe :)")
            print(f"Your change is {total_amount - coffe_price}")
            enough = True
        else:
            print("Please provide some more money..")

# TODO Crete reduce resources

# TODO Create Filin machine

def choose_from_menu():
    good_choice = False
    while good_choice == False:
        print("\nWhat would you like from menu?\n")
        menu_options = []
        extended_menu_options = []
        for i in MENU:
            print(i)
            menu_options.append(i)
            extended_menu_options.append(i)
            extended_menu_options.extend(special_commands)
        choice = (input("\nYour choice is: ")).lower()
        if choice in special_commands:
            print(f"\nSir, yes Sir.. {choice}")
            good_choice = True
        elif choice in menu_options:
            print(f"\nGood choice, {choice} it is!")
            good_choice = True
        elif choice not in extended_menu_options:
            print("\nYou need to chose something from the menu. Please try again..")
        #else:

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
        if my_choice in MENU:
            print("\nLets prepare some coffe.")
            if check_resources(my_choice):
                get_money(my_choice)


        


main()
