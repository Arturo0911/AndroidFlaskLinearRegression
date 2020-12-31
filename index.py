from flask import Flask
from flask import request, Response, jsonify

#----------------------------#
#      IMPORTS               #
#----------------------------#

from app import app 


if __name__ == "__main__":

    app.run(port=5000, debug=True)
    