import functools
from flask import request, abort, make_response, jsonify
from app.helpers.rest import *
import hmac
import hashlib


def login_required(func):
    """middleware to check login
    
    Arguments:
        func {function} -- function to be wrapped
    
    Returns:
        function -- wrapped function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if 'Application-Name' not in request.headers:
            abort(make_response(
                jsonify(response(400, 'Application-Name not Found')), 400))

        if request.headers['Application-Name'] != 'boilerplate':
            abort(make_response(
                jsonify(response(404, 'Invalid Application-Name')), 404))

        if 'Signature' not in request.headers:
            abort(make_response(
                jsonify(response(400, 'Invalid signature data')), 400))
        else:
            algo = hashlib.sha256
            data = bytes(request.base_url, 'UTF-8')
            secret = bytes(request.host_url, 'UTF-8')
            signature = hmac.new(secret, data, algo).hexdigest()
            print((data,secret,signature))
            if(request.headers['Signature'] != signature):
                abort(make_response(
                    jsonify(response(400, 'Invalid signature data')), 400))

        if 'Access-Token' not in request.headers:
            abort(make_response(
                jsonify(response(400, 'Invalid access token data')), 400))
        else:
            token_valid = validate(request.headers['Access-Token'])
            if token_valid['code'] != 200:
                abort(make_response(
                    jsonify(response(token_valid['code'], token_valid['message'])), 400))
        # print('masuk')
        return func(*args, **kwargs)
    return wrapper
