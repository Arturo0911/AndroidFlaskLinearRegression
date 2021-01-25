from app.helpers.check_passwords import password_hash
import graphene
from app.database.models import Employee
from app.database.models import Department
from app import db

from werkzeug.security import generate_password_hash, check_password_hash
# from app.database.schema import _Employee
from graphene_sqlalchemy import SQLAlchemyObjectType

class user_input(graphene.InputObjectType):

    credentials = graphene.String()
    names = graphene.String()
    last_names = graphene.String()
    phone_number = graphene.String()
    email_address = graphene.String()
    department_id = graphene.Int()
    department_name = graphene.String()
    username = graphene.String()
    password = graphene.String()



class Register_employee(graphene.Mutation):

    class Arguments:
        employee_data = user_input()
        
    # employee = graphene.Field(lambda:_Employee)

    def mutate(self,info,employee_data):

        employee = Employee(
            credentials = employee_data.credentials, names= employee_data.names, last_names= employee_data.last_names, 
            phone_number=employee_data.phone_number, email_address = employee_data.email_address, 
            department_id= employee_data.department_id,department_name = employee_data.department_name,
            username= employee_data.username,password = employee_data.password)
            


        db.session.add(employee)
        db.session.commit()

        return Register_employee(employee= employee)



"""class Register_department(Mutation):

    pass
"""



class Mutation(graphene.ObjectType):
    
    register_employee = Register_employee.Field()