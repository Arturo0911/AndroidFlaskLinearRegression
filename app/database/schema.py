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

"""class SearchResult(SQLAlchemyObjectType):
    class Meta:
        model = _Employee
"""


class Register_employee(graphene.Mutation):

    class Arguments:
        credentials = graphene.String(required=True)
        names = graphene.String(required=True)
        last_names = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        email_address = graphene.String(required=True)
        department_id = graphene.Int(required=True)
        department_name = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        
    employee = graphene.Field(lambda:_Employee)

    def mutate(self,info,credentials, names, last_names, phone_number, email_address,department_id, department_name,
    username, password):
        
        # department_id = Department.query.filter_by(department_name = department_name).first()

        employee = Employee(
            credentials = credentials, names= names, last_names= last_names, 
            phone_number=phone_number, email_address = email_address, 
            department_id= department_id,department_name = department_name,
            username= username,password = str(generate_password_hash(password)))
            
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
    search = graphene.Field(_Employee, q= graphene.String())
    # employee_by_credential = graphene.Field(Employee, credential= graphene.String(required=True))
    # employee_find_one = _Employee.
    all_departmnets = SQLAlchemyConnectionField(_Department, name = graphene.String())
    all_employee = SQLAlchemyConnectionField(_Employee, name = graphene.String())
    all_products = SQLAlchemyConnectionField(_Product, name = graphene.String())
    all_sales = SQLAlchemyConnectionField(_Sales, name = graphene.String())

    def resolve_search(self, info, **args):

        q = args.get("q")
        employee_query = _Employee.get_query(info)

        employees = employee_query.filter(Employee.credentials == q).first()

        return employees



schema = graphene.Schema(query= Query, mutation = Mutation,types=[_Employee, _Department, _Product, _Sales])
