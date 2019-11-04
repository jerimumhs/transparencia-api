from sqlalchemy.dialects.postgresql import UUID

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True)
