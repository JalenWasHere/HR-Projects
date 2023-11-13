import os
import sys
import json

'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''


def display(addressbook: list):
    print(addressbook)


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''


def list_contacts(addressbook):
    # todo: implement this function
    for contact in addressbook:
        print("Position: " + str(contact["id"]))
        print("First name: " + contact["first_name"])
        print("Last name: " + contact["last_name"])
        print("Emails: " + ",".join(contact["emails"]))
        print("Phone numbers: " + ",".join(contact["phone_numbers"]))
    return main('contacts.json')


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact(addressbook):
    # todo: implement this function
    print("Contact first name:")
    first_name = input(">>")
    print("Contact last name:")
    last_name = input(">>")
    print("Contact emails (separate by comma):")
    emails = input(">>")
    print("Contact phone numbers (separate by comma):")
    phone_numbers = input(">>")

    new_contact = {
        "id": len(addressbook) + 1,
        "first_name": first_name,
        "last_name": last_name,
        "emails": emails.split(","),
        "phone_numbers": phone_numbers.split(",")
    }

    addressbook.append(new_contact)
    write_to_json('contacts.json', addressbook)

    return main('contacts.json')


'''
remove contact by ID (integer)
'''


def remove_contact(contact):
    # todo: implement this function
    ...
    return contact


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts():
    # todo: implement this function
    ...


'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''


def quit_program(addressbook):
    quit()


def main(json_file):
    menu = [
        {"key": "L", "name": "List contacts", "function": list_contacts},
        {"key": "A", "name": "Add contact", "function": add_contact},
        {"key": "R", "name": "Remove contact", "function": remove_contact},
        {"key": "M", "name": "Merge contacts", "function": merge_contacts},
        {"key": "Q", "name": "Quit program", "function": quit_program}
    ]
    addressbook = read_from_json(json_file)

    for option in menu:
        print("[" + option["key"] + "] " + option["name"])
    selection = input(">>")
    for i, option in enumerate(menu):
        if selection.upper() in menu[i]["key"]:
            return menu[i]["function"](addressbook)

'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
