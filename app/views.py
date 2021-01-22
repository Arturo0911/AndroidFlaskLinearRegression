from flask.wrappers import Response
from app import app
from bson import json_util
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from os.path import isdir

# from database import Process
from error_handlers import Error_server
from app.helpers.check_passwords import generate_password_hash
from app.helpers.check_passwords import confirm_password
from app.database.schema import schema
from app.modeling_algorithm import modeling_initializer
from app.modeling_algorithm.libs import CSV
from app.modeling_algorithm.libs import API_values
from app.modeling_algorithm.libs.Create_days import Create_days
from app.modeling_algorithm.libs import Interface_objects
from app.modeling_algorithm.creating_process import Init_test
from app.modeling_algorithm.creating_process import init
from flask_graphql import GraphQLView

from app.database.Process import insert_data







@app.route("/", methods=['GET'])
def index():

    return jsonify({
        "Information": {
            'data direction': ' https://www.weatherbit.io/api/weather-history-hourly'
        },
        "status": "Model prediction",
        "status code": 200
    })


@app.route("/api", methods=['POST'])
def api():

    if isdir('.csv'):
        pass
    else:
        modeling_initializer.initializer()
    return jsonify({

        'status':'generated successfully',
        'status code': 200
    })

    


@app.route("/model", methods=['GET'])
def presentation():
    
    init_test = Init_test()
    info_test = init()

    return jsonify({
        'info': str(info_test),
        'info_values': 'process'
        #'init': str()
    })


@app.route("/test_graphql", methods=['GET','POST'])
def test_graphql():

    if request.method == 'POST':

        try:
            object_data = {
                'credentials': request.json['credentials'],
                'name': request.json['name'],
                'last_name': request.json['last_name'],
                'phone_number': request.json['phone_number'],
                'email_address': request.json['email_address'],
                'apartment': request.json['apartment'],
                'username': request.json['username'],
                'password': generate_password_hash(request.json['password']),
            }

            insert_data(object_data['credentials'],object_data['name'],
            object_data['last_name'],object_data['phone_number'],
            object_data['email_address'],object_data['apartment'],
            object_data['username'],object_data['password'])

            return jsonify({'status': 'data was saved successfully'})

        except Exception as e:
            return jsonify({'status': 'error by: '+str(e)})
        
    else:
        
        return jsonify({'status': 'nothing to show'})



app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
           'graphql',schema = schema,graphiql=True # Habilita la interfaz GraphiQL
       )
   )




# signup
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
                                                     username, password_hashed)
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
            "username": response_jsoned[0]['username'],
            "Name": response_jsoned[0]['name']

        }
        object_response = json_util.dumps(object_response)
        if check_passwords.confirm_password(password, password_hashed):
            return Response(object_response, mimetype='application/json')
        else:
            return jsonify({
                'status': "error in credentials"
            })
    except Exception as e:
        return jsonify({'status': 'Error by: '+str(e)})


@app.route("/android", methods=['GET', 'POST'])
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
                "password": password
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

            'status': 'GET',
            'status_code': 200
        })
