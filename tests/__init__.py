import psycopg2
from decouple import config
from flask_testing import TestCase
from sqlalchemy.exc import OperationalError

from app import app, db


class BaseTestCase(TestCase):
    db = None

    @classmethod
    def create_all(cls):
        try:
            cls.db.engine.execute("SELECT 1")
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
            cls.db.create_all()

    @staticmethod
    def create_app_test():
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

    @classmethod
    def clean_db(cls):
        for table in reversed(cls.db.metadata.sorted_tables):
            cls.db.session.execute(table.delete())

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        cls.app = cls.create_app_test()
        cls.db = db
        cls.create_all()

    @classmethod
    def tearDownClass(cls):
        cls.db.drop_all()
        super(BaseTestCase, cls).tearDownClass()

    def create_app(self):
        return self.app

    def setUp(self):
        super(BaseTestCase, self).setUp()

        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.clean_db()

    def tearDown(self):
        self.db.session.rollback()
        self.app_context.pop()

        super(BaseTestCase, self).tearDown()


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
            path += f'?{_filter}'
        return path
