# Imports
from main import AddressBook

# Start the app
while True:
    print('Select an option: ')
    print('a) See Address Book\nb) Add an Entry\nc) Update an Entry\nd) Delete an Entry')
    opt = input('Your selection: ').lower()
    while opt != 'a' and opt != 'b' and opt != 'c' and opt != 'd':
        print('Please make a valid selection.')
        print('a) See Address Book\nb) Add an Entry\nc) Update an Entry\nd) Delete an Entry')
        opt = input('Your selection: ').lower()

    # See Address Book
    if opt == 'a':
        # Placeholder Log
        print("See Address Book")
        # Pseudo Code
        book = AddressBook.select()
        for entry in book:
            print(AddressBook.select())

    # Add Entry to Address Book
    if opt == 'b':
        # Placeholder Log
        print("Add Entry")
        # Pseudo Code
        # Add Name
        name_add = input('Please enter a name: ')
        while len(name_add) == 0:
            name_add = input('Please enter a name: ')
        # Add address (can be blank)
        address_add = input('Please enter an address: ')
        # Add zipcode - must be 5 characters
        zipcode_add = input('Please enter a zip code: ')
        while len(address_add) > 0 and len(zipcode_add) != 5:
            zipcode_add = input('Please enter a valid zip code: ')
        # Primary Phone - must be 10 Digits
        primary_phone_add = int(input('Please enter a 10-digit primary phone number: '))
        while len(primary_phone_add) != 10:
            primary_phone_add = input('Please enter a 10-digit primary phone number: ')
        # Add emergency contact, can be skipped or needs a yes or no
        emergency_contact_add = input('Is this an emergency contact yes (y) or no (n)').lower()
        while emergency_contact_add != 'y' and emergency_contact_add != 'yes' and  emergency_contact_add != 'n' and  emergency_contact_add != 'no' and  emergency_contact_add != '':
            emergency_contact_add = input('Is this an emergency contact yes (y) or no (n)').lower()
        if emergency_contact_add == 'y' or emergency_contact_add == 'yes':
            emergency_contact_add = True
        else:
            emergency_contact_add = False
        # Add entry to Address Book
        AddressBook(name=name_add, address=address_add, zipcode=zipcode_add, primary_phone=primary_phone_add, emergency_contact=emergency_contact_add).save()
    # Edit Entry in Address Book
    if opt == 'c':
        print("Edit Entry")
    
    # Delete Entry in Address Book
    if opt == 'd':
        print('Delete Entry')

    run_again = input('Would you like to continue (c) or exit? (x): ').lower()
    if run_again == 'x':
        break