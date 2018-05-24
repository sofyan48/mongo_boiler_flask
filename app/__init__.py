import os
from . import configs
from flask import Flask
from werkzeug.contrib.cache import MemcachedCache
from flask_cors import CORS
from flask_mongoengine import MongoEngine

db = MongoEngine()
cache = MemcachedCache(['{}:{}'.format(os.getenv('MEMCACHE_HOST'), os.getenv('MEMCACHE_PORT'))])

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs.Config)

    #NOT FIX -> HARUS DIMASUKAN KE ENV
    app.config['MONGODB_DB'] = 'mongoboilerplate'
    app.config['MONGODB_HOST'] = 'localhost'
    app.config['MONGODB_PORT'] = 27017
    #########

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    from .controllers import api_blueprint
    from .controllers import swaggerui_blueprint

    app.register_blueprint(swaggerui_blueprint, url_prefix=os.getenv('SWAGGER_URL'))
    app.register_blueprint(api_blueprint)

    return app
