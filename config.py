import os


class Config(object):
    # FLASK
    DEBUG = False
    TESTING = False 
    # JWT
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = 20
    JWT_REFRESH_TOKEN_EXPIRES = 1800
    SECRET_KEY = 's3nh4-d01d4'


class ProductionConfig(Config):
    # FLASK
    DEBUG = False
    # POSTGRES
    SQLALCHEMY_DATABASE_URI = 'postgres://root:s3nh4@0.0.0.0:5432/transparencia?client_encoding=utf8'


class DevelopmentConfig(Config):
    # FLASK
    TESTING = True 
    DEBUG = True
    # POSTGRES
    SQLALCHEMY_DATABASE_URI = 'postgres://0.0.0.0:5432/transparencia-dev?client_encoding=utf8'


class TestingConfig(Config):
    # FLASK
    TESTING = True
    DEBUG = False
    # POSTGRES
    SQLALCHEMY_DATABASE_URI = 'postgres://0.0.0.0:5432/transparencia-test?client_encoding=utf8'


config = {
    "development": "config.DevelopmentConfig",
    "test": "config.TestingConfig",
    "production": "config.ProductionConfig",
    "default": "config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'test')
    app.config.from_object(config[config_name])
