import os

def create_contact(name, phone, email):
    contact = f"{name},{phone},{email}\n"
    with open("contacts.txt", "a") as file:
        file.write(contact)

def display_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("Contacts:")
                for contact in contacts:
                    print(contact.strip())
            else:
                print("No contacts found.")
    else:
        print("Contacts file does not exist.")

def search_contact(keyword):
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            found_contacts = [contact.strip() for contact in contacts if keyword.lower() in contact.lower()]
            if found_contacts:
                print(f"Search results for '{keyword}':")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found for '{keyword}'.")
    else:
        print("Contacts file does not exist.")

def delete_contact(keyword):
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        with open("contacts.txt", "w") as file:
            deleted = False
            for contact in contacts:
                if keyword.lower() not in contact.lower():
                    file.write(contact)
                else:
                    deleted = True
            if deleted:
                print(f"Contact(s) containing '{keyword}' deleted successfully.")
            else:
                print(f"No contacts found for '{keyword}'.")
    else:
        print("Contacts file does not exist.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            create_contact(name, phone, email)
            print("Contact added successfully.")

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            search_contact(keyword)

        elif choice == "4":
            keyword = input("Enter keyword to delete: ")
            delete_contact(keyword)

        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
