
from flask import request, abort
from functools import wraps


def requires_body(fields=''):
    def requires_body_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            body = request.get_json()

            if not body:
                abort(400, 'No request body provided')

            body_fields = fields.split(' ')

            for field in body_fields:
                if field not in body:
                    abort(400, f'Missing field: \'{field}\' in request body')

            return f(*args, **kwargs)

        return wrapper
    return requires_body_decorator
