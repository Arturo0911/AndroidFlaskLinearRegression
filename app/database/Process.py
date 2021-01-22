"""
Store in Mongo db
"""

from flask.wrappers import Response
# from app import mongo
from bson import json_util

from app.database.models import Users
# Queries

"""
    @param credentials 
    @param name = db.StringField(required = True)
    @param last_name = db.StringField(required = True)
    @param phone_number = db.StringField(required = True)
    @param email_address = db.StringField(required = True)
    @param department = db.StringField(required = True)

    @param username = db.StringField(required = True)
    @param password = db.StringField(required = True)
"""

def insert_data(credentials, name, 
            last_name,phone_number,
            email_address, department, 
            username,password):
    user = Users(credentials = credentials, name = name, last_name = last_name,
    phone_number = phone_number, email_address = email_address, department = department,
    username = username, password = password)

    user.save()





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

def find_one_element(username):
    # find one element using the parameter as filter
    # SELECT FROM <tabla name> WHERE <column name> = ${parameter}

    element_finded = mongo.db.users.find({'username': username,})
    return element_finded


def delete_element(parameter):
    # Delete one element using the parameter as filter
    # DELETE FROM <table name> WHERE <column name > is parameter


    pass
