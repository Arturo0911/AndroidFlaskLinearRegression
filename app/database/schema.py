from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
# importing the object models in the models file
from app.database.models import Employee
from app.database.models import Department
from app.database.models import Product
from app.database.models import Sales


class _Employee(SQLAlchemyObjectType):


    class Meta:

        model = Employee
        interfaces = (graphene.relay.Node, )


class Create_employee():
    pass


class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()
    employee = SQLAlchemyConnectionField(_Employee, name = graphene.String())

schema = graphene.Schema(query= Query, types=[_Employee])
