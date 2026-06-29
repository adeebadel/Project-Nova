# ============================================
#           PROJECT NOVA
#             Version 0.0.5
# ============================================

print("=" * 50)
print("        WELCOME TO PROJECT NOVA")
print("=" * 50)

print()

# -------------------------------
# User Setup
# -------------------------------

name = input("Enter your name: ")
college = input("Enter your college: ")
course = input("Enter your course: ")
graduation = input("Enter your graduation year: ")
dream_job = input("Enter your dream job: ")

print("\nProfile Created Successfully!\n")

# -------------------------------
# Main Menu
# -------------------------------

print("=" * 50)
print("               MAIN MENU")
print("=" * 50)

print("1. View Profile")
print("2. Study Tracker")
print("3. Exit")

print()

choice = int(input("Choose an option: "))

print()

# -------------------------------
# Decision Making
# -------------------------------

if choice == 1:

    print("=" * 50)
    print("YOUR PROFILE")
    print("=" * 50)

    print("Name        :", name)
    print("College     :", college)
    print("Course      :", course)
    print("Graduation  :", graduation)
    print("Dream Job   :", dream_job)

elif choice == 2:

    print("=" * 50)
    print("STUDY TRACKER")
    print("=" * 50)

    python_hours = float(input("Python Hours : "))
    math_hours = float(input("Math Hours   : "))
    ai_hours = float(input("AI Hours     : "))

    total = python_hours + math_hours + ai_hours

    print()
    print("Today's Progress")
    print("----------------")
    print("Python :", python_hours)
    print("Math   :", math_hours)
    print("AI     :", ai_hours)
    print("Total  :", total)

elif choice == 3:

    print("Thank you for using Project NOVA.")
    print("See you tomorrow!")

else:

    print("Invalid Option!")