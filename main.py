# ======================================
# PROJECT NOVA
# Version 0.0.7
# ======================================

def show_profile():

    print("\nPROFILE")
    print("-" * 40)

    print("Name :", name)
    print("College :", college)
    print("Course :", course)
    print("Graduation :", graduation)
    print("Dream Job :", dream_job)


def study_tracker():

    print("\nSTUDY TRACKER")

    python_hours = float(input("Python Hours : "))
    math_hours = float(input("Math Hours : "))
    ai_hours = float(input("AI Hours : "))

    total = python_hours + math_hours + ai_hours

    print("\nToday's Total :", total)


print("=" * 50)
print("WELCOME TO PROJECT NOVA")
print("=" * 50)

name = input("Name : ")
college = input("College : ")
course = input("Course : ")
graduation = input("Graduation : ")
dream_job = input("Dream Job : ")

running = True

while running:

    print("\n1. View Profile")
    print("2. Study Tracker")
    print("3. Exit")

    choice = int(input("\nChoose : "))

    if choice == 1:

        show_profile()

    elif choice == 2:

        study_tracker()

    elif choice == 3:

        print("Goodbye,", name)
        running = False

    else:

        print("Invalid Choice")