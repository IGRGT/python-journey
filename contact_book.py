import json


history = []
def new_contact(name, phone, email):
    add_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(add_contact)

def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"Contact {name} deleted.")
            return True
    print(f"No contact found with the name {name}.")
    return False

class contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                self.name = data["name"]
                self.phone = data["phone"]
                self.email = data["email"]
        except FileNotFoundError:
            self.name = name
            self.phone = phone
            self.email = email


try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = []
while True:

    print()
    print()
    print()
    print()
    topic = input("Welcome to the contact book! What would you like to do? ")
    print()
    history.append(topic)

    if topic == "add":
        print()
        print("Add a new contact")
        print()
        name = input("Please enter your name: ")
        phone = input("Please enter your phone number: ")
        email = input("please enter your email adress: ")
        new_contact(name, phone, email)
        print(f"Contact {name} added successfully.")
    elif topic == "delete":
        print()
        print("Delete a contact")
        print()
        contact_to_delete = input("Which contact would you like to delete? : ")
        delete_contact(contact_to_delete)
    elif topic == "view":
        print()
        print("View contacts")
        print()
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone']}, Email Adress: {contact['email']}")

    elif topic == "history":
        print()
        print("View history")
        print()
        for item in history:
            print(item)

    elif topic == "exit":
        print()
        print("Thanks for using the contact book! Until next time!")
        break
    else:
        print("Invalid input. Please try again.")
        continue

    with open("contacts.json", "w") as file:
        json.dump(contacts, file)