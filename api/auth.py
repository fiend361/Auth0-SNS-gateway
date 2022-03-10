import os

from functools import wraps
from flask import request, abort

from jose import jwt


ALGORITHMS = ['HS256']
SUBJECT = os.environ.get('TOKEN_SUBJECT', 'auth0')
AUDIENCE = os.environ.get('TOKEN_AUDIENCE', 'auth0_sns_gateway')
SECTRET_KEY = os.environ.get('TOKEN_SECRET_KEY', 'ofienrowfbpro0rw87fb0w48bfe948f2')


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401, 'Unauthorized. Request lacks valid authentication credentials.')

    token = request.headers['Authorization'].split(' ')

    if len(token) != 2:
        abort(401, 'Unauthorized. Request lacks valid authentication credentials.')

    elif token[0].lower() != 'bearer':
        abort(401, 'Unauthorized. Request lacks valid authentication credentials.')

    return token[1]


def verify_decode_jwt(token):
    try:
        payload = jwt.decode(
            token,
            SECTRET_KEY,
            algorithms=ALGORITHMS,
            subject=SUBJECT,
            audience=AUDIENCE
        )
        return payload
    
    except jwt.ExpiredSignatureError:
        abort(401, 'Token has expired.')

    except jwt.JWTClaimsError:
        abort(401, 'Incorrect claims. Please, check the subject and the audience.')

    except Exception:
        abort(400, 'Invalid header. Unable to parse authentication token.')


def requires_auth():
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            
            payload = verify_decode_jwt(token)
                
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator