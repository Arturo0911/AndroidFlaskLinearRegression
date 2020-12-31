from flask import Flask
from database import connection
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = connection.connection()
mongo = PyMongo(app)
from app import views