# Imports


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
        print("See Address Book")
    # Add Entry to Address Book
    if opt == 'b':
        print("Add Entry")
    # Edit Entry in Address Book
    if opt == 'c':
        print("Edit Entry")
    # Delete Entry in Address Book
    if opt == 'd':
        print('Delete Entry')

    run_again = input('Would you like to continue (c) or exit? (x): ').lower()
    if run_again == 'x':
        break