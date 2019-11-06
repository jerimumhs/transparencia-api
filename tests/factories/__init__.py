import uuid

from factory import lazy_attribute
from factory.alchemy import SQLAlchemyModelFactory

from app import db
from models.base import BaseModel


class BaseModelFactory(SQLAlchemyModelFactory):

    class Meta:
        model = BaseModel
        abstract = True
        sqlalchemy_session = db.session

    id = lazy_attribute(lambda x: uuid.uuid4())
