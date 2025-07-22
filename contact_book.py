contacts = []

def show_menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact {name} added successfully.")

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Found: {contact['name']} - {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
            contact['phone'] = input(f"Enter new phone (or press Enter to keep '{contact['phone']}'): ") or contact['phone']
            contact['email'] = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ") or contact['email']
            contact['address'] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
