from decouple import config as decouple_config


class Config(object):
    # FLASK
    DEBUG = False
    TESTING = False
    # JWT
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = 20
    JWT_REFRESH_TOKEN_EXPIRES = 1800
    SECRET_KEY = 's3nh4-d01d4'

    # POSTGRES
    DB_HOST = decouple_config('DB_HOST', 'postgres')
    DB_PORT = decouple_config('DB_PORT', 5432)
    DB_NAME = decouple_config('DB_NAME', 'postgres')
    DB_USER = decouple_config('DB_USER', 'postgres')
    DB_PASSWORD = decouple_config('DB_PASSWORD', 'postgres')
    SQLALCHEMY_DATABASE_URI = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?client_encoding=utf8'


class ProductionConfig(Config):
    # FLASK
    DEBUG = False


class DevelopmentConfig(Config):
    # FLASK
    TESTING = True
    DEBUG = True


class TestingConfig(Config):
    # FLASK
    TESTING = True
    DEBUG = False


config = {
    "development": "config.DevelopmentConfig",
    "test": "config.TestingConfig",
    "production": "config.ProductionConfig",
    "default": "config.DevelopmentConfig"
}


def configure_app(app):
    config_name = decouple_config('FLASK_ENV', 'test')
    app.config.from_object(config[config_name])
