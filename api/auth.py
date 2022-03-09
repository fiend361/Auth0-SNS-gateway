import json
from flask import request, abort
from functools import wraps
from jose import jwt


AUTH0_DOMAIN = 'fiend361.us.auth0.com'
ALGORITHMS = ['RS256']
subject = 'auth0'
audience = 'Coffee'
key = 'tg098j34g0n#2p9b738d2-4324r634234rd346rdf34wdqefrfq34rf43qrfdq23fq3*4frf'


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)
        raise AuthError({
            'code': 'Unauthorized',
            'description': 'Request lacks valid authentication credentials.'
        }, 401)

    token = request.headers['Authorization'].split(' ')

    if len(token) != 2:
        abort(401)
        raise AuthError({
            'code': 'Unauthorized',
            'description': 'Request lacks valid authentication credentials.'
        }, 401)

    elif token[0].lower() != 'bearer':
        abort(401)
        raise AuthError({
            'code': 'Unauthorized',
            'description': 'Request lacks valid authentication credentials.'
        }, 401)

    return token[1]


def verify_decode_jwt(token):
    try:
        payload = jwt.decode(
            token,
            key,
            algorithms=ALGORITHMS,
            subject=subject,
            audience=audience
        )

        return payload
    
    except jwt.ExpiredSignatureError:
        abort(401)
        raise AuthError({
            'code': 'token_expired',
            'description': 'Token expired.'
        }, 401)

    except jwt.JWTClaimsError:
        abort(401)
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Incorrect claims. Please, check the audience and issuer.'
        }, 401)
    except Exception:
        abort(400)
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Unable to parse authentication token.'
        }, 400)


def requires_auth():
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            
            try:
                payload = verify_decode_jwt(token)
            except:
                abort(401)
                
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator