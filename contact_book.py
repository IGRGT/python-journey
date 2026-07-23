
#Simple contact book program that allows users to add, delete, edit, search, and view contacts. The program also keeps a history of user actions and saves the contacts to a JSON file.

from datetime import datetime

import json


history = []
def new_contact(name, phone, email):
    new_entry = {"name": name, "phone": phone, "email": email, "date": timestamp()}
    contacts.append(new_entry)

def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted.")
            return True
    print(f"No contact found with the name {name}.")
    return False

def search_contact(name):
    found_contacts = [contact for contact in contacts if name.lower() in contact["name"].lower()]
    if found_contacts:
        print("Matched Contacts:")
        print()
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone']}, Email Adress: {contact['email']}, Date of Creation: {contact.get ('date', 'unknown')}")
            print()
        return True
    else:       
        print(f"No contacts found with the name {name}.")
        return False

def edit_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
                new_name = input("Enter the new name: ")
                new_phone = input("Enter the new phone number: ")
                new_email = input("Enter the new email address: ")
                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email
                print(f"Contact {name} was saved successfully.")
                return True
    print(f"No contact was found with the name {name}.")
    return False

def add_contact(name, phone, email):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"the contact {name} is already on the book")
            return False
    else:
        new_contact(name, phone, email)
        print(f"Contact {name} added successfully.")
        return True

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

def count_contacts():
    return len(contacts)



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
    history.append(f" Topic: {topic}, time of request: {timestamp()}")

    if topic == "add":
        print()
        name = input("Please enter your name: ")
        while name == "":
            print("That is not a valid name")
            name = input("Please enter your name: ")
        phone = input("Please enter your phone number: ")
        while not phone.isdigit() or len(phone) != 10:
            print("That is not a valid phone number, please try again")
            phone = input("Please enter yoyr phone number: ")
        email = input("please enter your email adress: ")
        while email == "":
            print("that is not a valid email")
            email = input("please enter your email adress: ")
        print()
        add_contact(name, phone, email)

    elif topic == "delete":
        print()
        print("Delete a contact")
        print()
        contact_to_delete = input("Which contact would you like to delete? : ")
        delete_contact(contact_to_delete)
        

    elif topic == "edit":
        print()
        print("Edit a Contact")
        print()
        contact_to_edit = input("Which contact would you like to edit? : ")      
        edit_contact(contact_to_edit)

    elif topic == "search":
        print("-----" * 50)
        print()
        print("Search the Database for a Contact")
        print()
        search_name = input("Please enter the name of the contact you woud like to search for: ")
        search_contact(search_name)

    elif topic == "view":
        print()
        print("View contacts")
        print()
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone']}, Email Adress: {contact['email']}, Date: {contact.get ('date', 'unknown')}")
            print()
        if not contacts:
            print("No contacts found.")
        else:
            print("Contacts displayed successfully.")

    elif topic == "count":
        print()
        print(f"You have {count_contacts()} contacts.")
        print()


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
