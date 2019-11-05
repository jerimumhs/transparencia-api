import psycopg2
from sqlalchemy.exc import OperationalError
from flask_testing import TestCase
from decouple import config

from app import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.update(
            TESTING=True,
            DEBUG=True,
            PRESERVE_CONTEXT_ON_EXCEPTION=False,
            SQLALCHEMY_DATABASE_URI=f""
                                    f"postgres://"
                                    f"{config('DB_USER')}:"
                                    f"{config('DB_PASSWORD')}@"
                                    f"{config('DB_HOST')}:"
                                    f"{config('DB_PORT', cast=int)}/"
                                    f"{config('DB_TEST_NAME', default='test')}?client_encoding=utf8"
        )
        return app

    def setUp(self):
        try:
            db.engine.execute("SELECT 1")
        except OperationalError:
            con = psycopg2.connect(
                dbname=config('DB_NAME'),
                host=config('DB_HOST'),
                port=config('DB_PORT'),
                user=config('DB_USER'),
                password=config('DB_PASSWORD')
            )
            con.autocommit = True

            cur = con.cursor()
            cur.execute(f"CREATE DATABASE {config('DB_TEST_NAME', default='test')};")
        finally:
            db.create_all()
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
