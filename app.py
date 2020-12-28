from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/meteor")
def meteor():
    return jsonify({"latitude":"-2.335017", "longitude":'-80.229769'})


if __name__ == "__main__":

    app.run(port=5000, debug=True)