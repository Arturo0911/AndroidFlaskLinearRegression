from flask import Flask
# from database import connection
from flask_pymongo import PyMongo

from app.database.connection import initialize_app
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/PureMango'
}

initialize_app(app)
# mongo = PyMongo(app)
from app import views