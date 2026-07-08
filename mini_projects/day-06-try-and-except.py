# 🛠️ Mini Project (Easy)
# Create:
# mini_projects/day16_calculator.py
# Requirements:
# Ask for two numbers.
# Add them.
# Use try and except.
# If the user enters text, print:
# ❌ Please enter valid numbers.
# That's it.
# 🎯 Easy Challenge
# Take yesterday's Journal project.
# If the user enters:
# hello
# instead of
# 1
# or
# 2
# Don't let the program crash.
# Use try and except.
# That's all.
try:
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    print(num1 + num2)
except:
    print("Invalid input")
    

