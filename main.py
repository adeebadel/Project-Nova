# ==========================================
# PROJECT NOVA
# Version 0.0.8
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

    print("\nToday's Total:", total)


def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    print("✅ Task Added Successfully!")


def view_tasks():

    if len(tasks) == 0:
        print("No Tasks Yet!")

    else:

        print("\n====== YOUR TASKS ======")

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


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
    print("5. Exit")

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
        print("Goodbye,", name)
        running = False

    else:
        print("Invalid Choice!")