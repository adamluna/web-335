# ========================================
# Title: luna-user-service.py
# Author: Adam Luna
# Date: 16 May 2021
# Description: Query and Create Documents in MongoDB using Python and pymongo.
# ========================================

# Import MongoClient, pprint, and datetime
from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# Create new user document
user = {
    "first_name": "Adam",
    "last_name": "Luna",
    "email": "adam@adam.com",
    "employee_id": "1010101",
    "date_created": datetime.datetime.utcnow()
}

# Insert new user focument
user_id = db.users.insert_one(user).inserted_id

# Output user id
print(user_id)

# Print the document returned from the FindOne Query
pprint.pprint(db.users.find_one({"employee_id": "1010101"}))
