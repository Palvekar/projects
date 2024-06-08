import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def rate(self, contacts, start=1):
        for index, contact in enumerate(contacts, start=start):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, search_name):
        found_contacts = []
        for contact in self.contacts:
            if search_name.lower() in contact.name.lower():
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

    def save_to_file(self, filename):
        data = [{"name": contact.name, "phone": contact.phone, "email": contact.email} for contact in self.contacts]
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.contacts = [Contact(contact["name"], contact["phone"], contact["email"]) for contact in data]

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Load Contacts")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)
            print("Contact added!")

        elif choice == "2":
            print("\nContacts:")
            contact_book.view_contacts()

        elif choice == "3":
            search_name = input("Enter name to search: ")
            print("\nSearch Result:")
            found_contacts = contact_book.search_contact(search_name)
            if found_contacts:
                for index, contact in enumerate(found_contacts, start=1):
                    print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            else:
                print("No contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                updated_contact = Contact(name, phone, email)
                contact_book.update_contact(index, updated_contact)
                print("Contact updated!")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted!")
            else:
                print("Invalid index.")

        elif choice == "6":
            filename = input("Enter the filename to save contacts: ")
            contact_book.save_to_file(filename)
            print("Contacts saved to file!")

        elif choice == "7":
            filename = input("Enter the filename to load contacts from: ")
            contact_book.load_from_file(filename)
            print("Contacts loaded from file!")

        elif choice == "8":
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
