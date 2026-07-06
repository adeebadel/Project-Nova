#Ask Email
#↓
#Remove Spaces
#↓
#Convert Lowercase
#↓
#Check @
#↓
#Check .
#↓
#Print Valid or Invalid

email = input("Enter your mail ID :")
print(email.strip())
print(email.lower())
print("@" in email)
print("." in email)
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")