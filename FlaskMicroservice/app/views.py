from flask.wrappers import Response
from app import app
from app import db
from bson import json_util
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from os.path import isdir
from concurrent.futures import ThreadPoolExecutor
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

from app.model.Model_prediction import initialize_model
from app.model.initializing import Init_test as init_testing
from pprint import pprint


@app.route("/", methods=['GET'])
def index():

    return jsonify({
        "Information": {
            'data direction': ' https://www.weatherbit.io/api/weather-history-hourly'
        },
        "status": "Model prediction",
        "status code": 200
    })


@app.route("/api", methods=['GET','POST'])
def api():

    if request.method == "POST":
        if isdir('.csv'):
            pass
        else:
            modeling_initializer.initializer()
        return jsonify({

            'status':'generated successfully',
            'status code': 200
        })
    else:
        
        result = schema.execute("""
                    {
            allEmployee {
                edges {
                node {
                    employeeId
                    names
                    lastNames
                    
                }
                }
            }
            }
        """)
    
    for x in result.data['allEmployee']['edges']:
        print(x['node']['employeeId'], x['node']['names'], x['node']['lastNames'])


    return jsonify({

            'status':'generated successfully',
            'status code': 200
        })

    


@app.route("/model", methods=['GET'])
def presentation():
    
    # init_test = Init_test()
    # info_test = init()

    return jsonify({
        'info': str("ok"),
        'info_values': 'process'
        #'init': str()
    })

@app.route("/testing", methods=['GET'])
def testing():
    
    if isdir(".prediction"):
        pass
    else:
        initialize_model()

    test_init = init_testing()

    # init_test = Init_test()
    coefficients_general, positive, negative = Init_test()._comparative_between_three_years()
    coefficients = test_init._comparative_between_three_years()
    # executor = ThreadPoolExecutor(max_workers=2)

    actual_prediction = init(coefficients['Overcast_clouds'][0]['2021']['x'], coefficients['Overcast_clouds'][0]['2021']['y'])['porcentaje_precision']
    desire_prediction = init(coefficients_general['Overcast_clouds'][1]['Overcast_clouds']['2018']['x'], 
    coefficients_general['Overcast_clouds'][1]['Overcast_clouds']['2018']['y'])['porcentaje_precision']


    if actual_prediction >= desire_prediction:

        status_ventas = float("{0:2f}".format(((actual_prediction/desire_prediction) *100) - 100))
    else:
        status_ventas = float("{0:2f}".format(((actual_prediction/desire_prediction) *100) - 100))

    return jsonify({
        "message" :'initialize model',
        'porcentaje_precision_actual':actual_prediction,
        "prediction_optima": desire_prediction,
        "Porcentaje de ganancías": status_ventas 
        })

# init(coefficients_general['Overcast_clouds'][1]['Overcast_clouds']['2018']['x']



"""
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
"""







app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
           'graphql',schema = schema,graphiql=True # Habilita la interfaz GraphiQL
    )
)

