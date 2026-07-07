# ==========================================
# PROJECT NOVA
# Version 0.3.0
# ==========================================

tasks = []


# ==========================
# FUNCTIONS
# ==========================

def show_profile():

    print("\n========== PROFILE ==========")
    print("Name :", profile["name"])
    print("College :", profile["college"])
    print("Course :", profile["course"])
    print("Graduation :", profile["graduation"])
    print("Dream Job :", profile["dream_job"])


def study_tracker():

    python_hours = float(input("Python Hours: "))
    math_hours = float(input("Math Hours: "))
    ai_hours = float(input("AI Hours: "))

    total = python_hours + math_hours + ai_hours

    print("\nToday's Total Study Hours:", total)


def add_task():

    task_name = input("Enter Task: ").strip().title()
    priority = input("Priority (High/Medium/Low): ").strip().title()

    task = {
        "name": task_name,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)

    print("✅ Task Added!")


def view_tasks():

    if len(tasks) == 0:
        print("No Tasks Yet!")
        return

    print("\n========== TASKS ==========")

    number = 1

    for task in tasks:

        print(f"{number}. {task['name']}")
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print()

        number += 1


def complete_task():

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks()

    choice = int(input("\nTask Number to Complete: "))

    if 1 <= choice <= len(tasks):

        tasks[choice - 1]["status"] = "Completed"

        print("✅ Task Completed!")

    else:

        print("❌ Invalid Task Number!")


def search_task():

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    keyword = input("Enter task to search: ").strip().lower()

    found = False

    for task in tasks:

        if keyword in task["name"].lower():

            print("\n✅ Found Task")
            print("Task      :", task["name"])
            print("Priority  :", task["priority"])
            print("Status    :", task["status"])

            found = True

    if not found:
        print("❌ Task Not Found")


def rename_task():

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks()

    choice = int(input("\nTask Number: "))

    if 1 <= choice <= len(tasks):

        new_name = input("New Task Name: ").strip().title()

        tasks[choice - 1]["name"] = new_name

        print("✅ Task Renamed Successfully!")

    else:

        print("❌ Invalid Task Number!")


# ==========================
# MAIN PROGRAM
# ==========================

print("=" * 50)
print("WELCOME TO PROJECT NOVA")
print("=" * 50)

profile = {

    "name": input("Name: ").strip().title(),
    "college": input("College: ").strip().title(),
    "course": input("Course: ").strip().title(),
    "graduation": input("Graduation: ").strip(),
    "dream_job": input("Dream Job: ").strip().title()

}

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

    choice = int(input("\nChoose: "))

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

        print("\nGoodbye,", profile["name"])
        running = False

    else:

        print("❌ Invalid Choice!")