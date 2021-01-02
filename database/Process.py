"""
Store in Mongo db
"""

from flask.wrappers import Response
from app import mongo
from bson import json_util


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
    # this method is to find any element
    # using the identification parameter

    parameters_finded = mongo.db.users.find()
    response = json_util.dumps(parameters_finded)
    return response
    #return Response(response, mimetype='application/json')