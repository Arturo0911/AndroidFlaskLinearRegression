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
    # INSERT INTO <table name>

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
    # this method is to find all elements
    # SELECT * FROM <table name>;

    parameters_finded = mongo.db.users.find()
    response = json_util.dumps(parameters_finded)
    return response
    #return Response(response, mimetype='application/json')

def find_one_element(parameter):
    # find one element using the parameter as filter
    # SELECT FROM <tabla name> WHERE <column name> = ${parameter}
    pass


def delete_element(parameter):
    # Delete one element using the parameter as filter
    # DELETE FROM <table name> WHERE <column name > is parameter


    pass