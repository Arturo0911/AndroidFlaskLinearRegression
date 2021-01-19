#!/usr/bin/python3
import asyncio
from app import app
from werkzeug.security import generate_password_hash, check_password_hash


def password_hash(password):

    password_hashed =  generate_password_hash(password)
    return str(password_hashed)



def confirm_password(password, password_hashed):

    return check_password_hash(password_hashed, password)








