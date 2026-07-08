import random

while True:
    print("\n===== DICE ROLLER =====")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("🎲 You rolled:", random.randint(1, 6))

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")