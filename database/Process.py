"""
Store in Mongo db
"""

from app import mongo


# Queries
def insert_data_MONGODB(name, identification,username, password):
    # to store main data into the db
    # the id filed is to identification as cedula or dni
    # in some places

    usersId = mongo.db.users.insert(
        {   
            "identification":identification,
            "username": username,
            "name": name,
            "password":password
        }
    )

    return usersId

def find_data_MONGODB():
    pass