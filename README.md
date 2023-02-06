# Address Book Command Line Project

## Description

This program provides an easy simple way to store contact information utilizing the commandline (as the front end) and SQL (backend)

## Setting Up the Program

### 1) Starting Out

Run the virtual Environment
```
pipenv shell
```

You can also run SQL if you would like to see the entries directly in the database
```
psql
```

### 2) Seed the File (Optional - See Below)

If you are running the program for the first time or you would like to erase all entries, seed the file with the following code
```
lib/seed.py
```

### 3) Install dependencies and Run the Program

In the virtual environment, type the following:
```
pip install peewee
pip install psycopg2-binary 
pip install autopep8 
python3 lib/addressbook.py
```

## Running the Program

The program allows for 4 basic commands:

1) See all entries
2) Add an entry
3) Edit an entry
4) Delete an entry

To get started, run the program in the virtual environment (step 3 above) by typing:
```
python3 lib/addressbook.py
```

Follow the prompts and viola!

## Field Requirements

**Name Field**: All entries in the Name field must be unique

**Address Field**: An address is not required

**Zip Code**: A zip code is not required so long as an address is not present.  If however, an address is included a 5-digit zip code is required.

**Phone Number**: A primary phone number is required for all entries

**Emergency Contact**: An emergency contact designation is not required; however, if this is skipped it will default to `False`

## Adding, Updating, and Deleting Contacts

### Adding

When adding a contact, the requirements are as per the Field Requirements noted above

### Updating

To start a user is prompted to provide a person's name in the Address Book.  Based on this selection, the terminal will walk you through each field to update.  If you wish to maintain the current information, simply press `ENTER` to skip the update on that field.  

*Note: If a user edits an address, they will be required to enter a zip code as well*

### Deleting

A user is prompted to provide the person's name for the entry they wish to delete.  

*Note: Since all names in the address book must be unique, the entry is case-sensitive*

## Future Features

- Add delete functionality for individual fields (for example, currently if an address exists you cannot remove it - only replace it)
- Include additional fields such as a second phone field, email address, website, etc.
- Provide user ability to select/control fields



