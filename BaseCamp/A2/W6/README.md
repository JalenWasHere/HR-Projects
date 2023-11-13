Create an application that manages contacts in an addressbook.

###### Menu structure:

```
[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program
```

###### Criteria:

- Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'), multiple (unique) phone numbers (only digits).  
    Also, an ID should be generated which should be 1 higher than the highest current ID.
- Remove a contact by ID.
- List all contacts with the option to sort by first\_name or last\_name (default first\_name) with a sort\_by parameter and in ascending (ASC) or decending (DESC) direction (default ASC) witb a direction parameter.
- Merge duplicate contacts (automatically). Contacts with the exact same full name (first and last name combined) should be merged.  
    _The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID).  
    The other duplicate contcts should be deleted from the addressbook._
- Contacts are read from the provided JSON file and should be updated with new or removed contacts.

###### Input example (add):

```
A
Firstname: John
Lastname: Doe
Emails: john@doe.com, john.doe@private.com
Phonenumbers: 0612345678, 010-1234567
```

###### Output example (\[A\] add):

`Contact added to addressbook`

###### Output example (\[L\] list contacts):

```
======================================
Position:  1
First name:  John
Last name:  Doe
Emails:  john@doe.com, john.doe@private.com
Phone numbers:  0612345678, 010-1234567
======================================Position: 2First name: PeterLast name: ParkerEmails: peter@parker.mePhone numbers: 0677345678....
```