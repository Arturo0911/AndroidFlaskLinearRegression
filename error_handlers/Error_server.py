from app import app
from flask import jsonify, Response, render_template


@app.errorhandler(404)
def not_found(error = None):
    
    error_message = {
        'message': 'request not avaliable',
        'status': 404
    }
    response = jsonify(error_message)
    response.status_code = 404

    return response

@app.
def error_authentication():
    
    try:
        pass

    except:

        pass

    return None
