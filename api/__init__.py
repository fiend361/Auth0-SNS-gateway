#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import (Flask, jsonify)
from flask import request as req

from api.auth import requires_auth
from api.request import requires_body

import api.sns as sns

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

app.config.from_pyfile('config.py')

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/send_otp', methods=['POST'])
@requires_auth()
@requires_body('recipient body')
def send_otp():
    body = req.get_json()
    target_phone_number = body['recipient']
    message = body['body']
    
    message_id, status_code = sns.publish_text_message(phone_number=target_phone_number, 
                                                       message=message)
    
    return jsonify({
        'success': True,
        'message_id': message_id,
        'status_code': status_code
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
    
@app.errorhandler(500)
def error_500(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': error.description
    }), 500
    