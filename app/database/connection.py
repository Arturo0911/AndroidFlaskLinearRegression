"""
MONGODB DATABASE CONNECTION
"""

from flask_mongoengine import MongoEngine

def connection():
    
    URI_CONNECTION = 'mongodb://localhost:27017/PureMango'
    
    return URI_CONNECTION


db = MongoEngine()

def initialize_app(app):
    
    db.init_app(app)
    pass
