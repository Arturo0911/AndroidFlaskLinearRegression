#!/usr/bin/python3

# mutation.py

import graphene
from app.database.models import Users
from app.database.schema import UserSchema

class Mutation(graphene.ObjectType):
    
    create_user = UserSchema.mutate
    

class Create_user(graphene.Mutation):

    user = graphene.Field(Users)

    def mutate(self):
        pass

