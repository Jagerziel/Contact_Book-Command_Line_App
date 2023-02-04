# Imports


# Start the app
while True:
    print('Select an option: ')
    print('a) See Address Book\nb) Add an Entry\nc) Update an Entry\nd) Delete an Entry\n')
    opt = input('Your selection: ').lower()
    while opt != 'a' and opt != 'b' and opt != 'c' and opt != 'd':
        print('Please make a valid selection.')
        print('a) See Address Book\nb) Add an Entry\nc) Update an Entry\nd) Delete an Entry\n')
        opt = input('Your selection: ').lower()
    break;