#!/usr/bin/python3

# mutation.py

import graphene


class Mutation(graphene.ObjectType):
    
    create_user = UserSchema.mutate

