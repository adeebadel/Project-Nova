#Create:
#mini_projects/day11_phonebook.py
#Requirements
#Create a dictionary like this:
#contacts = {
#    "Adeeb": "9876543210",
#   "Rahul": "9123456789",
#  "Aisha": "9988776655"
#}
#Ask the user:
#Enter Contact Name:
#If the name exists:
#Phone Number:
#Otherwise:
#Contact Not Found
#💡 Hint: Use:
#if name in contacts:
# mini_projects/day11_phonebook.py

contacts = {
    "Adeeb": "9876543210",
    "Rahul": "9123456789",
    "Aisha": "9988776655"
}

name = input("Enter Contact Name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact Not Found")