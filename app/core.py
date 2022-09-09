from flask import request, jsonify


def token_required(func):
    def function_wrapper(*args, **kwargs):
        if request.headers.get('Authorization') == 'o030101':
            return func(*args, **kwargs)
        return jsonify({'error': 'token is not valid'}), 401

    return function_wrapper