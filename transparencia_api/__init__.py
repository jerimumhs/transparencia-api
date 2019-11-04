from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger
from dynaconf import FlaskDynaconf

from transparencia_api.resources import add_resources


app = Flask(__name__)
CORS(app)
FlaskDynaconf(app)
api = Api(app, prefix='/api/v1')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
swagger = Swagger(app)


add_resources(api)
