from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
from graphql import GraphQLError
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


# class to get login acces from android client
class Login_user(graphene.Mutation):

    status_message= graphene.Boolean(description= "Request status")
    body_message = graphene.String(description = "Request message")
    employee = graphene.Field(_Employee)

    class Input:
        username = graphene.String(description="User's")
        password = graphene.String(description="User's password")


    def mutate(self, info, username, password):

        try:
            vrerify_user = Employee.query.filter_by(username = username).first()
            if vrerify_user:

                if check_password_hash( vrerify_user.password,password):
                    status_message = True
                    body_message = "User verified"
                    return Login_user(
                        status_message = status_message,
                        body_message = body_message,
                        employee = vrerify_user
                        )
            else:
                raise Exception("credenciales incorrectas") 
        except Exception as e:
            raise GraphQLError("No se puede verificar el usuario")

class Update_user(graphene.Mutation):

    status_message= graphene.Boolean(description= "Request status")
    body_message = graphene.String(description = "Request message")
    # employee = graphene.Field(_Employee)

    class Input:
        credentials = graphene.String(required=True)
        names = graphene.String(required=True)
        last_names = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        email_address = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, credentials, 
        names, last_names, phone_number, 
            email_address, username, password):

            try:
                verify_employee = Employee.query.filter_by(credentials = credentials).first()
                verify_employee.names = names
                verify_employee.last_names = last_names
                verify_employee.phone_number = phone_number
                verify_employee.email_address = email_address
                verify_employee.username = username
                verify_employee.password = generate_password_hash(password)

                status_message = True
                body_message = "Empleado actualizado satisfactoriamente"
                # db.session.add(verify_employee)
                db.session.commit()
                return Update_user(
                    status_message = status_message,
                    body_message = body_message
                )

            except Exception as e:
                pass


class Mutation(graphene.ObjectType):
    
    register_employee = Register_employee.Field()
    login_user = Login_user.Field()
    update_user = Update_user.Field()

class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()
    search = graphene.Field(_Sales, q= graphene.String())
    # search_sales_time = graphene.Field(_Sales, q = graphene.String())
    all_departmnets = SQLAlchemyConnectionField(_Department, name = graphene.String())
    all_employee = SQLAlchemyConnectionField(_Employee, name = graphene.String())
    all_products = SQLAlchemyConnectionField(_Product, name = graphene.String())
    all_sales = SQLAlchemyConnectionField(_Sales, name = graphene.String())

    """def resolve_search_sales(self, info, **args):
        q = args.get("q")
        sales_query = _Sales.get_query(info)
        sales = sales_query.filter(Sales.product_name == q).first()
        return sales
    """
    def resolve_search(self, info, **args):

        q = args.get("q")
        sales_query = _Sales.get_query(info)
        sales = sales_query.filter(Sales.time_start == q).first()
        return sales



schema = graphene.Schema(query= Query, mutation = Mutation,types=[_Employee, _Department, _Product, _Sales])
