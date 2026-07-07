contacts = [
    {"name": "Adeeb", "phone": "9876543210"}
]


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully")


def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(contact["name"], "-", contact["phone"])


print("1. Add Contact")
print("2. View Contacts")
print("3. Exit")
choice = input("Choose an option: ")

if choice == "1":
    add_contact()
elif choice == "2":
    view_contacts()
else:
    print("Goodbye")
