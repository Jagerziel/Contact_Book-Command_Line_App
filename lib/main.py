# import datetime
import datetime

# NOTE--START<<<BOILER PLATE FOR PEEWEE>>>
# Import peewee
from peewee import *

from playhouse.shortcuts import dict_to_model, model_to_dict

# Create database - specify db_name, user, password, host, and port
db = PostgresqlDatabase('address_book', user='jagerziel', password='12345',
    host='localhost', port=5432)


# Create base model to pull from database
class BaseModel(Model):
    class Meta:
        database = db

# NOTE--END <<<BOILER PLATE FOR PEEWEE>>>

# Create subclass
class AddressBook(BaseModel):
    name = CharField(unique=True)
    address = CharField()
    zipcode = CharField()
    primary_phone = CharField()
    emergency_contact = BooleanField()





