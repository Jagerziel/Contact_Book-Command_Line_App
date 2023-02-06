# Imports
from main import AddressBook
from playhouse.shortcuts import dict_to_model, model_to_dict

def pull_entries():
    all_entries = []
    for entries in AddressBook.select():        
        all_entries.append(model_to_dict(entries))
    return all_entries

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
        # Placeholder Tag
        print("Add Entry")
        # Pseudo Code
        # Add Name
        name_add = input('Please enter a name: ')
        while len(name_add) == 0:
            name_add = input('Please enter a name: ')
        # Add address (can be blank)
        address_add = input('Please enter an address: ')
        # Add zipcode - must be 5 characters, can skip if no address
        zipcode_add = int(input('Please enter a zip code: '))
        while len(address_add) > 0 and len(str(zipcode_add)) != 5:
            zipcode_add = int(input('Please enter a valid zip code: '))
        # Primary Phone - must be 10 Digits
        primary_phone_add = str(input('Please enter a 10-digit primary phone number: '))
        while len(primary_phone_add) != 10:
            primary_phone_add = str(input('Please enter a 10-digit primary phone number: '))
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
        print('Entry added')
    # Edit Entry in Address Book
    if opt == 'c':
        # Placeholder Tag
        print("Edit Entry")
        # Pseudo Code
        selected = ""  
        # Pull all entries into variable
        all_entries = pull_entries()
        # Iterate through all entries selecting the name (names must be unique)
        while selected == "":
            selection = input('Enter the name of the entry you would like to edit: ')
            for row in all_entries:
                if (selection == row['name']):
                    selected = row
                    break

        print(f"{selected['name']}'s record selected. Update information where desired, you may press ENTER to maintain current details")

        # NOTE: FIX FROM HERE DOWN

        # Edit Name
        name_edit = input(f'Please enter a name (current: {selected.name}): ')
        # Edit Address
        address_edit = input(f'Please enter an address (current: {selected.address}): ')
        # Edit Zip Code
        zipcode_edit = int(input(f'Please enter a zip code (current: {selected.zipcode}): '))
        while len(address_edit) > 0 and len(str(zipcode_edit)) != 5:
            zipcode_edit = int(input('Please enter a valid zip code: '))        
        # Edit Primary Phone
        primary_phone_edit = str(input(f'Please enter a 10-digit primary phone number (current: {selected.primary_phone}): '))
        while len(primary_phone_edit) != 10:
            primary_phone_edit =  str(input(f'Please enter a 10-digit primary phone number (current: {selected.primary_phone}): '))
        # Emergency Contact
        emergency_contact_edit = selected.emergency_contact
        if selected.emergency_contact == True:
            emergency_contact_edit = input(f'This entry is currently an emergency contact, would you like to remove designation? yes (y) or no (n) ').lower()
            if emergency_contact_edit == 'y' or emergency_contact_edit == 'yes':
                emergency_contact_edit = False
        if selected.emergency_contact == False:
            mergency_contact_edit = input(f'This entry is currently not an emergency contact, would you like to add designation? yes (y) or no (n) ').lower()
            if emergency_contact_edit == 'y' or emergency_contact_edit == 'yes':
                emergency_contact_edit = True
        # Update Entry
        AddressBook(name=name_edit, address=address_edit, zipcode=zipcode_edit, primary_phone=primary_phone_edit, emergency_contact=emergency_contact_add).save()

        print('Entry updated')
    
    # Delete Entry in Address Book
    if opt == 'd':
        # Placeholder Tag
        print('Delete Entry')
        # Pseudo Code
        selection = input('Enter the name of the entry you would like to edit: ')
        selected = AddressBook.delete_instance()
        print('Entry deleted')
    # Ask to run again
    run_again = input('Would you like to continue (c) or exit? (x): ').lower()
    while run_again != 'c' and run_again != 'x':
        run_again = input('Would you like to continue (c) or exit? (x): ').lower()
    if run_again == 'x':
        break