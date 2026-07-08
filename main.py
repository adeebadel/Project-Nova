# ==========================================
# PROJECT NOVA
# Version 0.3.0
# ==========================================
#import json: used to import the json library so that we can access each dictionary
#import random : random values will be provided for example for dice etc., and for lists and dictionaries random values from variables will be selected
import json
import random
from datetime import datetime
import os


tasks = []
profiles = []

quotes = [
    "Discipline beats motivation.",
    "Small progress every day.",
    "One bug at a time.",
    "Consistency creates success.",
    "Keep building."
]
#try and except: are useful to cause no errors in between for example a value asks number if we put a variable it will ensure to cause no error
if os.path.exists("tasks.json"):

    file = open("tasks.json", "r")

    tasks = json.load(file)

    file.close()

else:

    tasks = []
# ==========================
# FUNCTIONS
# ==========================
#from here def () function starts which defines an variable to process 
def show_profile(profile):

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


def add_task(tasks):

    task_name = input("Enter Task: ").strip().title()
    priority = input("Priority (High/Medium/Low): ").strip().title()

    task = {
    "name": task_name,
    "priority": priority,
    "status": "Pending",
    "created": datetime.now().strftime("%d-%m-%Y %I:%M %p")
}

    tasks.append(task)

    file = open("tasks.json", "w")

    json.dump(tasks, file, indent=4)

    file.close()
    print("✅ Task Added!")

def view_tasks(tasks):

    if len(tasks) == 0:
        print("No Tasks Yet!")
        return

    print("\n========== TASKS ==========")

    for number, task in enumerate(tasks, start=1):

        print(f"{number}. {task['name']}")
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("Created  :", task.get("created", "Unknown"))
        print()


def complete_task(tasks):

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks(tasks)
    try:
        choice = int(input("\nTask Number to Complete: "))

    except:
        print("❌ Invalid Number")
        return
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["status"] = "Completed"

        file = open("tasks.json", "w")
        json.dump(tasks, file, indent=4)
        file.close()

        print("✅ Task Completed!")
    else:
        print("❌ Invalid Task Number!")


def search_task(tasks):

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


def rename_task(tasks):

    if len(tasks) == 0:
        print("No Tasks Available!")
        return

    view_tasks(tasks)

    try:
        choice = int(input("\nTask Number: "))

    except:
        print("❌ Invalid Number")
        return

    if 1 <= choice <= len(tasks):

        new_name = input("New Task Name: ").strip().title()

        tasks[choice - 1]["name"] = new_name
        file = open("tasks.json", "w")
        json.dump(tasks, file, indent=4)
        file.close()

        print("✅ Task Renamed Successfully!")

    else:

        print("❌ Invalid Task Number!")
        
def view_all_profiles(profiles):

    if len(profiles) == 0:
        print("No Profiles Found!")
        return

    print("\n========== ALL PROFILES ==========")

    number = 1

    for person in profiles:

        print(number, ".", person["name"])
        print("College :", person["college"])
        print("Course  :", person["course"])
        print("Dream Job :", person["dream_job"])
        print()

        number += 1
        
def search_profile(profiles):

    keyword = input("Enter Name: ").strip().lower()

    found = False

    for person in profiles:

        if keyword in person["name"].lower():

            print("\nProfile Found")
            print(person)

            found = True

    if not found:
        print("Profile Not Found")
        
def motivation():

    print()
    print(random.choice(quotes))
    
def task_stats(tasks):

    print("\n====== TASK STATS ======")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    completed = [
        task
        for task in tasks
        if task["status"] == "Completed"
    ]

    print("Total Tasks:", len(tasks))
    print("Completed Tasks:", len(completed))
    print("Pending Tasks:", len(tasks) - len(completed))
    
def pending_tasks(tasks):

    print("\n====== PENDING TASKS ======")

    pending = [
        task
        for task in tasks
        if task["status"] == "Pending"
    ]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for number, task in enumerate(pending, start=1):

        print(f"{number}. {task['name']}")
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print()

# ==========================
# MAIN PROGRAM
# ==========================

print("=" * 50)
print("WELCOME TO PROJECT NOVA")
print("=" * 50)

print("Current Folder:")
print(os.getcwd())

profile = {

    "name": input("Name: ").strip().title(),
    "college": input("College: ").strip().title(),
    "course": input("Course: ").strip().title(),
    "graduation": input("Graduation: ").strip(),
    "dream_job": input("Dream Job: ").strip().title()

}
profiles.append(profile)

running = True

while running:

    print("""
╔══════════════════════════════════════════════════════╗
║                  🚀 PROJECT NOVA 🚀                 ║
╠══════════════════════════════════════════════════════╣
║  1. 👤 View Profile                                 ║
║  2. 📚 Study Tracker                                ║
║  3. ➕ Add Task                                     ║
║  4. 📋 View Tasks                                   ║
║  5. ✅ Complete Task                                ║
║  6. 🔍 Search Task                                  ║
║  7. ✏️ Rename Task                                  ║
║  8. 👥 View All Profiles                            ║
║  9. 🔎 Search Profile                               ║
║ 10. 💡 Daily Motivation                             ║
║ 11. 📊 Task Statistics                              ║
║ 12. ⏳ Pending Tasks                                ║
║ 13. ❌ Exit                                         ║
╚══════════════════════════════════════════════════════╝
""")
    try:
        choice = int(input("\nChoose: "))

    except:
        print("❌ Please enter a number.")
        continue

#please make sure to get all these while loops rights and these are used to choose from each value using for loops and while loops with else,elif,while,if
    if choice == 1:

        show_profile(profile)

    elif choice == 2:

        study_tracker()

    elif choice == 3:

        add_task(tasks)

    elif choice == 4:

        view_tasks(tasks)

    elif choice == 5:

        complete_task(tasks)

    elif choice == 6:

        search_task(tasks)

    elif choice == 7:

        rename_task(tasks)

    elif choice == 8:
        view_all_profiles(profiles)

    elif choice == 9:
        search_profile(profiles)

    elif choice == 10:
        motivation()

    elif choice == 11:
        task_stats(tasks)

    elif choice == 12:
        pending_tasks(tasks)

    elif choice == 13:
        print("\nGoodbye,", profile["name"])
        running = False