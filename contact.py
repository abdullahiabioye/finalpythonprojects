import os

# Function to display all contacts
def display_contacts():
    if os.path.exists("cont.txt"):
        with open("cont.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("Contacts List:")
                for contact in contacts:
                    print(contact.strip())
            else:
                print("No contacts found.")
    else:
        print("No contacts found.")

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open("cont.txt", "a") as file:
        file.write(f"{name}, {phone}, {email}\n")
    print("Contact added successfully.")

# Function to edit a contact
def edit_contact():
    name_to_edit = input("Enter the name of the contact to edit: ")
    contacts = []

    with open("cont.txt", "r") as file:
        contacts = file.readlines()

    with open("cont.txt", "w") as file:
        contact_found = False
        for contact in contacts:
            name, phone, email = contact.strip().split(", ")
            if name == name_to_edit:
                print(f"Editing contact: {contact.strip()}")
                new_name = input(f"Enter new name (or press enter to keep {name}): ") or name
                new_phone = input(f"Enter new phone number (or press enter to keep {phone}): ") or phone
                new_email = input(f"Enter new email (or press enter to keep {email}): ") or email
                file.write(f"{new_name}, {new_phone}, {new_email}\n")
                contact_found = True
            else:
                file.write(contact)
        
        if contact_found:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    contacts = []

    with open("cont.txt", "r") as file:
        contacts = file.readlines()

    with open("cont.txt", "w") as file:
        contact_found = False
        for contact in contacts:
            name, phone, email = contact.strip().split(", ")
            if name == name_to_delete:
                print(f"Deleting contact: {contact.strip()}")
                contact_found = True
            else:
                file.write(contact)

        if contact_found:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

# Function to search for a contact
def search_contact():
    name_to_search = input("Enter the name of the contact to search for: ")
    
    with open("cont.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            name, phone, email = contact.strip().split(", ")
            if name_to_search.lower() in name.lower():
                print(f"Contact found: {contact.strip()}")
                return
        
        print("Contact not found.")

# Main function to run the contact management system
def contact_manager():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Display all contacts")
        print("2. Add a new contact")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Search for a contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact manager
contact_manager()
