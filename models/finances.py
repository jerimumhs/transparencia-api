from enum import Enum

from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import validates

from models.base import db, BaseModel
from utils import ClassProperty


class Ticket(BaseModel):
    class TicketType(Enum):
        EXPENSE = 1
        INCOME = 2

    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    _type = db.Column(ChoiceType(TicketType, impl=db.Integer()), nullable=False)

    @validates('name', 'value', 'date', '_type')
    def validate_fields(self, key, value):
        if value in [None, '']:
            raise ValueError(f'O atributo {key} precisa ter um valor atribuido')

        if key == 'value':
            self.validate_value(key, value)

        return value

    @staticmethod
    def validate_value(key,  value):
        if value <= 0:
            raise ValueError(f'O atributo {key} precisa ter um valor positivo')

    @property
    def type(self):
        return self._type.value

    @type.setter
    def type(self, value):
        if not isinstance(value, self.TicketType):
            value = self.TicketType(value)
        self._type = value

    # noinspection PyMethodParameters
    @ClassProperty
    def expenses(cls):
        return cls.query.filter_by(_type=cls.TicketType.EXPENSE)

    # noinspection PyMethodParameters
    @ClassProperty
    def incomes(cls):
        return cls.query.filter_by(_type=cls.TicketType.INCOME)
