from flask import Flask
from flask import request, Response, jsonify

from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

# Imports from the database directory
from database import connection

"""
app = Flask(__name__)
app.config['MONGO_URI'] = connection.connection()
mongo = PyMongo(app)
"""
class Init_server():
    
    def __init__(self):
        """
        Create the variables to 
        generate the server
        """
        self.app = None
        self.mongo = None

    def app_connection(self):
        
        self.app = Flask(__name__)
        self.app.config['MONGO_URI'] = connection.connection()
        return self.app

    def mongo_connection(self):
        
        self.mongo = PyMongo(self.app())
        return self.mongo
    
    

"""
@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/about")
def about():
    return "holis"

@app.route("/holis")
def holis():
    return jsonify({
        'name': "Arturo Negreiros"
    })

@app.route("/testing")
def testing():

    return "I'm testing my server with docker"
"""
# Get methods
# @app.route("/meteor", methods=['GET'])
# def meteor():




# Mongo process

"""
# POST methods
@app.route("/prediction", methods=['POST'])
def prediction():
    station = request.json['station']
    clouds_quantity = request.json['clouds']

    

    try:
        if station and clouds_quantity:
            # return jsonify({"latitude":"-2.335017", "longitude":'-80.229769'})
            id = mongo.db.users.insert(
                {
                    'station':station,
                    'clouds': clouds_quantity
                }
            )
            response = jsonify({
                'status':'ok'
            })
            response.status_code = 201
            return response

    except Exception as e:
        return jsonify({'ErrorHandled': str(e)})
    else:
        pass
"""
        

if __name__ == "__main__":

    server = Init_server()
    app = server.app_connection()
    app.run(port=5000, debug=True)