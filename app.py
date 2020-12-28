from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Meteorology'
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/meteor", methods=['GET'])
def meteor():
    return jsonify({"latitude":"-2.335017", "longitude":'-80.229769'})


if __name__ == "__main__":

    app.run(port=5000, debug=True)