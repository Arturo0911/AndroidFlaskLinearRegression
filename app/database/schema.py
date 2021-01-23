import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType #,MongoSchema
from graphene_mongodb import MongoSchema
from app.database.models import Users as Users_model


#class Users_Schema(MongoSchema):
#    pass

# class Users(MongoengineObjectType):
class UserSchema(MongoSchema):
    # class Meta():
    description = "Users"
    model = Users_model
        # interfaces = (Node,)

class Query(graphene.ObjectType):
    
    user = UserSchema.single
    # node = Node.Field()
    # all_users = MongoengineConnectionField(Users)

schema = graphene.Schema(query = Query)#, types = [Users])


