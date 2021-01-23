#!/usr/bin/python3

# mutation.py

import graphene
from app.database.models import Users

class Mutation(graphene.ObjectType):
    
    create_user = UserSchema.mutate
    pass

class Create_user(graphene.Mutation):

    user = graphene.Field(Users)

    def mutate(self):
        pass

