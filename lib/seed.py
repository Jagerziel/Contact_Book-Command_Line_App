from main import *

# Connect to DB
db.connect()

# Create table with setup in the AddressBook class
db.drop_tables([AddressBook])
db.create_tables([AddressBook])

# Starting Data from Seed File
AddressBook(name="FirstName", address="1234 Street", zipcode=11230, primary_phone="1234567890", emergency_contact=False).save()
