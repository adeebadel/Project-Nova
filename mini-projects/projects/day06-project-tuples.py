#🏆 Challenge Project
#Create:
#mini_projects/day13_menu.py
#Requirements
#Create a tuple:
#MENU = (
    #   "Burger",
    #  "Pizza",
    # "Pasta",
    #"Fries",
    #"Coffee"
#)
#Display the menu using a for loop.
#Ask the user to enter a number.
#Print:
#You Ordered:
#Pizza

MENU = (
    "Burger",
    "Pizza",
    "Pasta",
    "Fries",
    "Coffee"
)

print("===== MENU =====")

number = 1

for item in MENU:
    print(number, ".", item)
    number += 1

choice = int(input("\nChoose a menu item (1-5): "))

print("You Ordered:", MENU[choice - 1])