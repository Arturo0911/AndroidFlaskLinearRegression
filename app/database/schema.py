import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType #,MongoSchema
from graphene_mongodb import MongoSchema
from app.database.models import Users as Users_model
from app.database.graphql.mutation import Mutation


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

class UserInput(graphene.InputObjectType):
    credentials = graphene.String()
    name = graphene.String()
    last_name = graphene.String()
    phone_number = graphene.String()
    email_address = graphene.String()
    department = graphene.String()
    username = graphene.String()
    password = graphene.String()


    



class create_User(graphene.Mutation):
    
    user = graphene.Field(Users_model)

    class Arguments:
        user_data = UserInput()

    def mutate(self):
        pass



schema = graphene.Schema(query = Query, mutation= Mutation)#, types = [Users])


