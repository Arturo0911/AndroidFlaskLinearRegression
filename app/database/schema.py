from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
# importing the object models in the models file
from app.database.models import Employee
from app.database.models import Department
from app.database.models import Product
from app.database.models import Sales
from app import db
# import mutations

# from app.database.graphql.mutation import Mutation
from werkzeug.security import generate_password_hash, check_password_hash



class _Department(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (graphene.relay.Node, )

class _Employee(SQLAlchemyObjectType):
    class Meta:

        model = Employee
        interfaces = (graphene.relay.Node, )

class _Product(SQLAlchemyObjectType):
    class Meta:
        
        model = Product
        interfaces = (graphene.relay.Node, )


class _Sales(SQLAlchemyObjectType):
    class Meta:

        model = Sales
        interfaces = (graphene.relay.Node, )



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
        
    employee = graphene.Field(lambda:_Employee)

    def mutate(self,info,employee_data):
        
        department_id = Department.query.filter_by(department_name = employee_data.department_name).first()

        employee = Employee(
            credentials = employee_data.credentials, names= employee_data.names, last_names= employee_data.last_names, 
            phone_number=employee_data.phone_number, email_address = employee_data.email_address, 
            department_id= department_id,department_name = employee_data.department_name,
            username= employee_data.username,password = str(generate_password_hash(employee_data.password)))
            
        db.session.add(employee)
        db.session.commit()

        return Register_employee(employee= employee)


class Mutation(graphene.ObjectType):
    
    register_employee = Register_employee.Field()

"""class Create_employee():
    pass
"""

class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()
    all_departmnets = SQLAlchemyConnectionField(_Department, name = graphene.String())
    all_employee = SQLAlchemyConnectionField(_Employee, name = graphene.String())
    all_products = SQLAlchemyConnectionField(_Product, name = graphene.String())
    all_sales = SQLAlchemyConnectionField(_Sales, name = graphene.String())

schema = graphene.Schema(query= Query, mutation = Mutation,types=[_Employee, _Department, _Product, _Sales])
