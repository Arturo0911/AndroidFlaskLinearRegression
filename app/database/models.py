

from app.database.connection import db

class Department(db.Document):

    meta = {'collections': 'department'}
    department_name = db.StringField(required=True)
    _id_employee = db.StringField(primary_key=True,required=True)


class Users(db.Document):

    meta = {'collections': 'users'}
    credentials = db.StringField(required = True)
    name = db.StringField(required = True)
    last_name = db.StringField(required = True)
    phone_number = db.StringField(required = True)
    email_address = db.StringField(required = True)
    department = db.StringField(required = True)
    username = db.StringField(required = True)
    password = db.StringField(required = True)





class Roles(db.Document):
    

    name = db.StringField(required = True)
    name = db.StringField(required = True)
    name = db.StringField(required = True)
    name = db.StringField(required = True)
    name = db.StringField(required = True)


