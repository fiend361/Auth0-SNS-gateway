#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import (Flask, jsonify)
from api.auth import requires_auth

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

app.config.from_pyfile('config.py')

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
@requires_auth()
def index():
    return jsonify({
        'hello': 'world',
    }), 200
    

#----------------------------------------------------------------------------#
# Error Handlers.
#----------------------------------------------------------------------------#

@app.errorhandler(400)
def error_400(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': error.description
    }), 400
    
@app.errorhandler(401)
def error_401(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': error.description
    }), 401

@app.errorhandler(404)
def error_404(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': error.description
    }), 404
    
@app.errorhandler(409)
def error_409(error):
    return jsonify({
        'success': False,
        'error': 409,
        'message': error.description
    }), 409
    
@app.errorhandler(500)
def error_500(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': error.description
    }), 500
    