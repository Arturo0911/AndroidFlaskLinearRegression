#!/usr/bin/python3

# mutation.py

import graphene
from app.database.models import Users
from app.database.schema import UserSchema, Query

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
    
    user = graphene.Field(Users)

    class Arguments:
        user_data = UserInput()

    def mutate(self, info, user_data):

        user = Users(
            credentials = user_data.credentials,
            name = user_data.name,
            last_name = user_data.last_name,
            phone_number = user_data.phone_number,
            email_address = user_data.email_address,
            department = user_data.department,
            username = user_data.username,
            password = user_data.password
        )
        user.save()

        return create_User(user=user)

# class Mutation(UserSchema.mutate):
    
#     create_user = create_User.Field()

    

"""class Create_user(graphene.Mutation):

    user = graphene.Field(Users)

    def mutate(self):
        pass
"""
