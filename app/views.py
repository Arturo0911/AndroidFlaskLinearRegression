from flask.wrappers import Response
from app import app
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from database import Process
from error_handlers import Error_server
#----------------------------#
#      ROUTES                #
#----------------------------#

@app.route("/")
def index():
    
    return jsonify({
            "status": "working api"
        })

@app.route("/home/<int:position>")
def home_page(position):
    # showing the position id

    return jsonify({
               
        "position": position
        })
    # return "this is your position id %s"%position


@app.route("/api", methods=['GET'])
def api():
        
    
    message = {
            "Id":"0918237421",
            "Name":"Arturo Francesco",
            "Lname": "Negreiros Samanez",
            "Age": 28,
            "Skills": "High"
        }

    print(message)
    return jsonify(message)

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

            if name and identification and password and username:

                password_hashed = generate_password_hash(password)
                userId = Process.insert_data_MONGODB(name, identification, 
                username,password_hashed)
                return jsonify({
                    'status': str(userId)
                })
            else:

                return Error_server.not_found()

        elif request.method == 'GET':
            
            answer = Process.find_data_MONGODB()
        

            return Response(answer, mimetype='application/json')
    except Exception as e:
        
        return jsonify({
                "status": str(e)
        })


@app.route("/android", methods=['GET','POST'])
def android():
    
    if request.method == "POST":
        print("the request method has been required")
        print(request.json)

        id = request.json['Id']:
            pass    
        else:
            pass    
        return jsonify({
                "status": "POST",
                "status_code": 200
            })
    else:
        return jsonify({
                
                'status':'GET',
                'status_code': 200
            })
    





