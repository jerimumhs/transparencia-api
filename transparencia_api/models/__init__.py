from loguru import logger

from transparencia_api import db


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True)

    @logger.catch
    def save(self):
        db.session.add(self)
        db.session.commit()

    @logger.catch
    def delete(self):
        db.session.delete(self)
        db.session.commit()
