#add()
#subtract()
#multiply()
#divide()
#Ask the user which operation they want.
#Call the correct function.

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    return a / b

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

choice = input("Enter your choice : =")

if choice == "1":
    print(addition(num1,num2))
elif choice == "2":
    print(subtraction(num1,num2))
elif choice == "3":
    print(multiply(num1,num2))
else:
    print(division(num1,num2))
    