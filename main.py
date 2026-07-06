# ==========================================
# PROJECT NOVA
# Version 0.0.9
# ==========================================

tasks = []

def show_profile():
    print("\n========== PROFILE ==========")
    print("Name :", name)
    print("College :", college)
    print("Course :", course)
    print("Graduation :", graduation)
    print("Dream Job :", dream_job)


def study_tracker():
    python_hours = float(input("Python Hours: "))
    math_hours = float(input("Math Hours: "))
    ai_hours = float(input("AI Hours: "))

    total = python_hours + math_hours + ai_hours

    print("Today's Total:", total)


def add_task():
    task = input("Enter Task: ").strip().title()
    tasks.append(task)
    print("✅ Task Added!")


def view_tasks():

    if len(tasks) == 0:
        print("No Tasks Yet!")

    else:

        print("\n====== TASKS ======")

        number = 1

        for task in tasks:
            print(number, ".", task)
            number += 1


def complete_task():

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks()

    choice = int(input("\nTask Number to Complete: "))

    if 1 <= choice <= len(tasks):

        completed = tasks.pop(choice - 1)

        print("✅ Completed:", completed)

    else:

        print("Invalid Task Number!")
        
def search_task():

    keyword = input("Enter task to search: ").strip().lower()

    found = False

    for task in tasks:

        if keyword in task.lower():

            print("✅ Found:", task)
            found = True
        if len(tasks) == 0:
            print("No Tasks Available!")
            return

    if not found:
        print("❌ Task not found.")
        
def rename_task():

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks()

    choice = int(input("Task Number: "))

    if 1 <= choice <= len(tasks):

        new_name = input("New Task Name: ").strip().title()

        tasks[choice - 1] = new_name

        print("✅ Task Renamed Successfully!")

    else:
        print("❌ Invalid Task Number!")


print("=" * 50)
print("WELCOME TO PROJECT NOVA")
print("=" * 50)

name = input("Name: ")
college = input("College: ")
course = input("Course: ")
graduation = input("Graduation: ")
dream_job = input("Dream Job: ")

running = True

while running:

    print("\n========== MAIN MENU ==========")

    print("1. View Profile")
    print("2. Study Tracker")
    print("3. Add Task")
    print("4. View Tasks")
    print("5. Complete Task")
    print("6. Search Task")
    print("7. Rename Task")
    print("8. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        show_profile()

    elif choice == 2:
        study_tracker()

    elif choice == 3:
        add_task()

    elif choice == 4:
        view_tasks()

    elif choice == 5:
        complete_task()

    elif choice == 6:
        search_task()

    elif choice == 7:
        rename_task()

    elif choice == 8:
        print("Goodbye,", name)
        running = False
    
    else:
        print("Invalid Choice!")
        
