from flask.wrappers import Response
from app import app
from app import db
from bson import json_util
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from os.path import isdir

# from database import Process
# from error_handlers import Error_server
from app.helpers.check_passwords import generate_password_hash
from app.helpers.check_passwords import confirm_password
# from app.database.schema import schema
from app.modeling_algorithm import modeling_initializer
from app.modeling_algorithm.libs import CSV
from app.modeling_algorithm.libs import API_values
from app.modeling_algorithm.libs.Create_days import Create_days
from app.modeling_algorithm.libs import Interface_objects
from app.modeling_algorithm.creating_process import Init_test
from app.modeling_algorithm.creating_process import init
from flask_graphql import GraphQLView
from app.database.schema import schema
# from app.database.Process import insert_data

from app.database.Process import login_resolve_process
from app.database.models import Employee




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

@app.route("/login_resolve", methods=['POST'])
def login_resolve():

    try:
        
        username = request.json['Username']
        password = request.json['Password']

        print(username, password)
        print(login_resolve_process(username, password))


        #print(login_resolve_process(username, password))
        #return jsonify({'message':'ok'})

    except Exception as e:
        # print("Aqui es el error")
        print(str(e))
        return jsonify({
            'error': str(e)
        })




app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
           'graphql',schema = schema,graphiql=True # Habilita la interfaz GraphiQL
    )
)

