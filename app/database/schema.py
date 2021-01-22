import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from app.database.models import Users as Users_model




class Users(MongoengineObjectType):
    
    class Meta():
        description = "Users"
        model = Users_model
        interfaces = (Node,)

class Query(graphene.ObjectType):

    node = Node.Field()
    all_users = MongoengineConnectionField(Users)

schema = graphene.Schema(query = Query, types = [Users])


