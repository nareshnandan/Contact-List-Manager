contacts = {}

def add_contact(name, number):
    """Adds a new contact."""
    contacts[name] = number
    print(f"Contact {name} added successfully.")

def delete_contact(name):
    """Deletes a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def view_contacts():
    """Displays all contacts."""
    if contacts:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts available.")

def contact_manager():
    """Main function to manage the contact list."""
    while True:
        print("\nContact List Manager")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            print("Exiting Contact List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact manager
contact_manager()
