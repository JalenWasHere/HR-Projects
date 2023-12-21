import json


class Contact:
    def __init__(self, contact_data):
        self.id = contact_data['id']
        self.first_name = contact_data['first_name']
        self.last_name = contact_data['last_name']
        self.emails = contact_data['emails']
        self.phone_numbers = contact_data['phone_numbers']

    def __str__(self):
        return f"Position: {self.id}\nFirst name: {self.first_name}\nLast name: {self.last_name}\n" \
               f"Emails: {', '.join(self.emails)}\nPhone numbers: {', '.join(self.phone_numbers)}\n"


class AddressBook:
    def __init__(self, contacts):
        self.contacts = []
        for contact_data in contacts:
            contact = Contact(contact_data)
            self.contacts.append(contact)

    def add_contact(self, first_name, last_name, emails, phone_numbers):
        contact_id = len(self.contacts) + 1
        contact_data = {
            'id': contact_id,
            'first_name': first_name,
            'last_name': last_name,
            'emails': emails,
            'phone_numbers': phone_numbers
        }
        self.contacts.append(Contact(contact_data))
        print("Contact added to addressbook")

    def remove_contact(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact.id != contact_id]
        print(f"Contact with ID {contact_id} removed from addressbook")

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)

    def merge_contacts(self):
        seen_full_names = set()
        merged_contacts = []

        for current_contact in self.contacts:
            full_name = f"{current_contact.first_name} {current_contact.last_name}"

            contact_found = False
            for existing_contact in merged_contacts:
                if f"{existing_contact.first_name} {existing_contact.last_name}" == full_name:
                    contact_found = True
                    self.merge_contact_info(existing_contact, current_contact)
                    break

            if not contact_found:
                seen_full_names.add(full_name)
                merged_contacts.append(current_contact)

        self.contacts = merged_contacts

    def merge_contact_info(self, existing_contact, new_contact):
        existing_contact.emails.extend(new_contact.emails)
        existing_contact.phone_numbers.extend(new_contact.phone_numbers)


def load_addressbook(filename):
    file = open(filename, 'r')
    data = json.load(file)
    address_book = AddressBook(data)
    return address_book


def save_addressbook(address_book, filename):
    data = [{'id': contact.id,
             'first_name': contact.first_name,
             'last_name': contact.last_name,
             'emails': list(contact.emails),
             'phone_numbers': list(contact.phone_numbers)} for contact in address_book.contacts]

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def main():
    filename = 'contacts.json'
    address_book = load_addressbook(filename)

    while True:
        print("\nMenu:")
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")

        choice = input("Select an option: ").upper()

        if choice == 'L':
            address_book.list_contacts()
        elif choice == 'A':
            first_name = input("First name: ")
            last_name = input("Last name: ")
            emails = input("Emails (seperate with comma): ").split(', ')
            phone_numbers = input("Phone numbers (seperate with comma): ").split(', ')
            address_book.add_contact(first_name, last_name, emails, phone_numbers)
        elif choice == 'R':
            contact_id = int(input("Enter the ID: "))
            address_book.remove_contact(contact_id)
        elif choice == 'M':
            address_book.merge_contacts()
            print("Contacts merged successfully")
        elif choice == 'Q':
            save_addressbook(address_book, filename)
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
