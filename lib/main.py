# import datetime
import datetime

# NOTE--START<<<BOILER PLATE FOR PEEWEE>>>
# Import peewee
from peewee import *

# Create database - specify db_name, user, password, host, and port
db = PostgresqlDatabase('people', user='postgres', password='12345',
    host='localhost', port=8000)

# Connect to DB
db.connect()

# Create base model to pull from database
class BaseModel(Model):
    class Meta:
        database = db

# NOTE--END <<<BOILER PLATE FOR PEEWEE>>>

# Create subclass
class AddressBook(BaseModel):
    name = CharField()
    address = CharField()
    zipcode = IntegerField()
    primary_phone = CharField()
    emergency_contact = BooleanField()

# Create table with setup in the AddressBook class
db.drop_tables([AddressBook])
db.create_tables([AddressBook])





