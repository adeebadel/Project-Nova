count = 1
while count <= 5:
    print(count)
    count = count + 1
    
#Correct PIN = 1234
#User has 3 attempts
#Correct PIN → Login Successful
#Wrong PIN → Try Again
#3 wrong attempts → Account Locked
# Hint:
#You'll need:
#while
#if

correct_pin = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break

    else:
        attempts = attempts + 1
        print("Wrong PIN. Try Again")

if attempts == max_attempts:
    print("Account Locked")