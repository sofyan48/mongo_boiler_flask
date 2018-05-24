from flask_restful import Resource, reqparse, fields, marshal_with
from app.models.account import *
from app.helpers.rest import *
from app.helpers.memcache import *
from app.middlewares.auth import login_required


class AccountCollectionResource(Resource):
    # @login_required
    def get(self):
        obj = []
        accounts = get_cache('accounts')
        if not accounts:
            accounts = Account.objects.all()
            for i in accounts:
                data = {
                    'id' : str(i.id),
                    'owner_email' : i.owner_email,
                    'first_name' : i.owner_firstname,
                    'last_name' : i.owner_lastname,
                    'state' : i.account_state
                }
                obj.append(data)
            set_cache('accounts', obj)
        return response(200, data=obj)


class AccountResource(Resource):
    # @login_required
    def get(self, account_id):
        account = get_cache('account_{}'.format(account_id))
        if not account:
            account = Account.objects.get(id=account_id)
            data = {
                'id' : str(account.id),
                'owner_email' : account.owner_email,
                'first_name' : account.owner_firstname,
                'last_name' : account.owner_lastname,
                'state' : account.account_state
            }
            set_cache('account_{}'.format(account_id), data)
        return response(200, data=data)


class AccountInsert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('state', type=str, required=True)
        args = parser.parse_args()

        owner_email = args['email']
        owner_firstname = args['first_name']
        owner_lastname = args['last_name']
        account_state = args['state']

        account = Account(owner_email=owner_email,
                            owner_firstname=owner_firstname,
                            owner_lastname=owner_lastname,
                            account_state=account_state)

        account.save()
        return response(200, data=args)
