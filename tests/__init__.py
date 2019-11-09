import psycopg2
from decouple import config
from flask_testing import TestCase
from sqlalchemy.exc import OperationalError

from app import app, db


class BaseTestCase(TestCase):
    @staticmethod
    def create_all():
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
            cur.execute(f"CREATE DATABASE "
                        f"{config('DB_TEST_NAME', default='test')};")
        finally:
            db.create_all()

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
                                    f"{config('DB_TEST_NAME', default='test')}"
                                    f"?client_encoding=utf8"
        )
        return app

    def setUp(self):
        db.session.remove()
        self.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class BaseAPITestCase(BaseTestCase):
    def setUp(self):
        super(BaseAPITestCase, self).setUp()
        self.endpoint = None

    def get_path(self, id_detail=None, action=None, _filter=None):
        if not self.endpoint:
            raise AttributeError('Endpoint não definido')
        path = f'/{self.endpoint}/'
        if id_detail:
            path += f'{id_detail}/'
        if action:
            path += f'{action}/'
        if filter:
            path += f'?{_filter or ""}'
        return path
