from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger
from decouple import config


app = Flask(__name__)
CORS(app)
app.config.update(
    DEBUG=config('FLASK_DEBUG', default=False, cast=bool),
    TESTING=config('FLASK_TESTING', default=False, cast=bool),
    ENV=config('FLASK_ENV', default='production'),

    JWT_TOKEN_LOCATION=['headers'],
    JWT_ACCESS_TOKEN_EXPIRES=20,
    JWT_REFRESH_TOKEN_EXPIRES=1800,
    JWT_HEADER_NAME='Authorization',
    JWT_HEADER_TYPE='Bearer',
    JWT_SECRET_KEY=config('JWT_SECRET_KEY'),

    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_DATABASE_URI=f""
                            f"postgres://"
                            f"{config('DB_USER')}:"
                            f"{config('DB_PASSWORD')}@"
                            f"{config('DB_HOST')}:"
                            f"{config('DB_PORT', cast=int)}/"
                            f"{config('DB_NAME')}?client_encoding=utf8",
    SWAGGER={
        "specs_route": "/",
        "title": "Transparência API",
        "description": "API para o portal de transparência do JerimumHS",
    }
)

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
swagger = Swagger(app)


from resources import add_resources

add_resources(api)
from models import *  # noqa F401
