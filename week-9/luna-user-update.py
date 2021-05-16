# ========================================
# Title: luna-user-update.py
# Author: Adam Luna
# Date: 16 May 2021
# Description: Update and delete documents in MongoDB using Python and pymongo.
# ========================================

# Import MongoClient, pprint and datetime
from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335

# Update the user document by changing the email field to your Bellevue Unviersity email address
db.users.update_one(
    {"employee_id": "1010101"},
    {
        "$set": {
            "email": "adluna@my365.bellevue.edu"
        }
    }
)

# Output email, employee_id, first_name and last_name using the findOne function
pprint.pprint(db.users.find_one({"employee_id": "1010101"}))