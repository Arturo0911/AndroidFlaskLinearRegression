#from app.database.graphql.mutation import Mutation
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType #,MongoSchema
from graphene_mongodb import MongoSchema
from app.database.models import Users as Users_model
#from app.database.graphql.mutation import Mutation
#from app.database.graphql.mutation import Mutation


# class Users_Schema(MongoSchema):
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

class Mutation(graphene.ObjectType):
    
    create_user = UserSchema.mutate

schema = graphene.Schema(query = Query, mutation= Mutation)

result = schema.execute("""
query Data {
  user(username: "John") {
    id
    username
  }
}""")