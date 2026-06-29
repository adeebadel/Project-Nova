# -----------------------------------
# PROJECT NOVA
# Version 0.0.3
# -----------------------------------

print("=" * 50)
print("WELCOME TO PROJECT NOVA")
print("=" * 50)

print()

# User Setup
name = input("Enter your name: ")
college = input("Enter your college: ")
course = input("Enter your course: ")
graduation = input("Graduation year: ")
dream_job = input("Dream job: ")

print()

print("=" * 50)
print("YOUR PROFILE")
print("=" * 50)

print("Name :", name)
print("College :", college)
print("Course :", course)
print("Graduation :", graduation)
print("Dream Job :", dream_job)

print()

print("Welcome to Project NOVA,", name)

print("=" * 50)


print("\n=== STUDY TRACKER ===")

python_hours = float(input("Python hours today: "))
math_hours = float(input("Math hours today: "))
ai_hours = float(input("AI hours today: "))

total_hours = python_hours + math_hours + ai_hours

print("\nToday's Summary")
print("Python:", python_hours)
print("Math:", math_hours)
print("AI:", ai_hours)
print("Total Hours:", total_hours)