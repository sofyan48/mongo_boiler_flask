from flask import Blueprint
from flask_restful import Api
from .account import *
# from .auth import *

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)
# api.add_resource(AuthLoginController, '/login')
# api.add_resource(AuthLogoutController, '/logout')
api.add_resource(AccountCollectionResource, '/accounts')
api.add_resource(AccountResource, '/accounts/<account_id>')
api.add_resource(AccountInsert, '/accounts')
