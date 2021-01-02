from flask.wrappers import Response
from app import app
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from database import Process

#----------------------------#
#      ROUTES                #
#----------------------------#

@app.route("/")
def index():
    return "welcome to our API prediction model"

@app.route("/home/<int:position>")
def home_page(position):
    # showing the position id
    return "this is your position id %s"%position


@app.route("/api")
def api():
    return jsonify({
            "Id": "0918237421",
            "Name": "Arturo",
            "Lname": "Negreiros Samanéz",
            "Age":28,
            "skills": "High",
            "Knowledge":["Python", "Java", "Javascript", "Docker", "Php"]
            })

@app.route("/model", methods=['POST'])
def presentation():
    name = request.json['name']
    print(name)

    try:
        if name:

            return jsonify({
                "status": "ok"
            })
        else:
            return jsonify({
                "status": "Server error"
            })
    except Exception as e:
        return jsonify({
            "exception": str(e)
        })


@app.route("/testing", methods=['GET', 'POST'])
def testing():

    try:

        if request.method == 'POST':
            
            identification = request.json['identification']
            name = request.json['name']
            username = request.json['username']
            password = request.json['password']
        
            if identification and password:

                password_hashed = generate_password_hash(password)
                userId = Process.insert_data_MONGODB(name, identification, 
                username,password_hashed)
                return jsonify({
                    'status': str(userId)
                })
            else:
                pass
        elif request.method == 'GET':
            
            answer = Process.find_data_MONGODB()

            return Response(answer, mimetype='application/json')
    except Exception as e:
        return jsonify({
            'status': "error by: "+str(e)
        })



