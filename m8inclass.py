
def add_contact(name, number, phonebook):
    if name in phonebook:
        print(f"Contact '{name}' already exists.")
    else:
        phonebook[name] = number
        print(f"Contact '{name}' added successfully.")


def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' does not exist.")


def update_contact(phonebook, name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' does not exist.")


def display_contacts(phonebook):
    if phonebook:
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")


def phonebook_menu():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1: Add Contact")
        print("2: Delete Contact")
        print("3: Update Contact")
        print("4: Display Contacts")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number, phonebook)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            delete_contact(phonebook, name)
        elif choice == "3":
            name = input("Enter contact name to update: ")
            number = input("Enter new contact number: ")
            update_contact(phonebook, name, number)
        elif choice == "4":
            display_contacts(phonebook)
        elif choice == "5":
            print("Exiting Phonebook Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


phonebook_menu()
