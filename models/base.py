import uuid

from loguru import logger
from sqlalchemy.dialects.postgresql import UUID

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    @logger.catch
    def save(self):
        db.session.add(self)
        db.session.commit()

    @logger.catch
    def delete(self):
        db.session.delete(self)
        db.session.commit()
