#!/usr/bin/python3
import asyncio
from app import app
from werkzeug.security import generate_password_hash, check_password_hash


async def password_hash(password):

    password_hashed = await generate_password_hash(password)
    return password_hashed



async def confirm_password(password, password_hashed):

    try:
        return await check_password_hash(password_hashed, password)
    except:
        return None








