import arrow
import hashlib
from uniqid import uniqid
from flask import request
from flask_restful import Resource, reqparse
from app.helpers.rest import *
from app.helpers.memcache import *
from app.libs import Ldap
from app.models.account_token import *
from app.models.account import *
from app.middlewares.auth import login_required

class AuthLoginController(Resource):
    def post(self):
        # return auths.validate('e45e22b1cc6dfe38bba1ce2190bfee4b')
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        account = get_account_by_email(args['email'])

        if account:
            if account['account_state'] == 'terminated':
                return response(401, 'Your account has been terminated'), 401

            if account['account_state'] == 'in-active':
                update_account_state('active',account['id'])

            params = {
                'username': account['username_ldap'],
                'password': args['password']
            }

            ldap = Ldap()
            connect = ldap.connect(params)
            print(connect)
            if 'error_code' in connect:
                if connect['error_code'] == 34:
                    message = 'User not found'
                elif connect['error_code'] == 49:
                    message = 'Invalid Credential'
                else:
                    message = 'Somethin went wrong'

                return response(401, message), 401
            else:
                now = arrow.now()

                token_limit = str(now.shift(
                    hours=+24).format('YYYY-MM-DD HH:mm:ss'))
                print(token_limit)
                result = get_account_token_by_account_id(account['id'])

                if result:
                    token = result['ldap_token']
                    update_account_token(result['id'], token_limit)
                else:
                    # print(hashlib.md5(uniqid('123')).hexdigest())
                    token = hashlib.md5(uniqid(account['username_ldap']).encode('utf-8')).hexdigest()
                    insert_account_token(account['id'], token, token_limit)
                
                return response(200, data={'token': token}), 200
                # check hostbill (not implemented yet)
        else:
            return response(401, 'There is no account associated with the email'), 401


class AuthLogoutController(Resource):
    @login_required
    def post(self):
        result = get_account_token_by_access_token(
            request.headers['Access-Token'])

        if result:
            now = str(arrow.now().format('YYYY-MM-DD HH:mm:ss'))
            update_account_token(result['id'], now)
            return response(200, 'Logout Success')
        else:
            return response(404, 'Invalid Token')
