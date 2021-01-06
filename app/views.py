from flask.wrappers import Response
from app import app
from bson import json_util
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import json


from database import Process
from error_handlers import Error_server
from app.helpers import check_passwords
#----------------------------#
#      ROUTES                #
#----------------------------#

@app.route("/", methods=['GET','POST'])
def index():
    
    """if request.method == 'POST':
        
    else:
        pass"""


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

                password_hashed = check_passwords.password_hash(password)
                print(password_hashed)
                userId = Process.insert_data_MONGODB(name, identification, 
                username,password_hashed)
                return jsonify({
                    'status': str(userId),
                    'status_code': 200
                })
            else:

                return Error_server.not_found()

        elif request.method == 'GET':
            answer = Process.find_data_MONGODB()
            print(type(answer))
            print(answer)
            return Response(answer, mimetype='application/json')
    except Exception as e:
        
        return jsonify({
                "status": str(e)
        })
@app.route("/auth/<username>/<password>", methods=['GET'])
def auth(username, password):
    try:
        # instance the method to find into Mongdb 
        # and create a variable to asign tha values.
        users_finded = Process.find_one_element(str(username))
        
        # Create the response variable to catch json query from Mongodb.
        # After that create two variables; one for use the json.loads function
        # and the another one to get the password hashed asigned
        response = json_util.dumps(users_finded)
        response_jsoned = json.loads(response)
        password_hashed = response_jsoned[0]['password']
        
        # credentials
        object_response = {
                "id_certification": response_jsoned[0]['identification'],
                "username":response_jsoned[0]['username'] ,
                "Name": response_jsoned[0]['name']

                }
        object_response = json_util.dumps(object_response)
        if check_passwords.confirm_password(password, password_hashed):
            return  Response(object_response, mimetype='application/json')
        else:
            return jsonify({
                    'status': "error in credentials"
                })
    except Exception as e:
        return jsonify({'status': 'Error by: '+str(e) })






@app.route("/android", methods=['GET','POST'])
def android():
    
    if request.method == "POST":
        print("the request method has been required")
        print(request.json)

        fullname = request.json['Fullname']
        email = request.json['Email']
        password = generate_password_hash(request.json['Password'])

        if fullname and email and password:

            object_to_store = {

                    "fullname": fullname,
                    "email": email, 
                    "password":password
                    }
            print(object_to_store)
            return jsonify({

                "status": "POST ok",
                "status_code": 200
                    
                })
        else:
            return Error_server.not_found()   
    else:
        return jsonify({
                
                'status':'GET',
                'status_code': 200
            })
    





