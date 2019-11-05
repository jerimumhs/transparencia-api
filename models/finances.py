from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import validates

from models.base import db, BaseModel
from utils import ClassProperty


class Ticket(BaseModel):
    EXPENSE = 'e'
    INCOME = 'i'
    TYPES = [
        (EXPENSE, 'Gasto'),
        (INCOME, 'Renda')
    ]

    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    _type = db.Column(ChoiceType(TYPES), nullable=False)

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
        if value not in [t[0] for t in self.TYPES]:
            raise ValueError(f'Os possíveis valores para o type são: {[t[0] for t in self.TYPES]}')
        self._type = value

    # noinspection PyMethodParameters
    @ClassProperty
    def expenses(cls):
        return cls.query.filter_by(_type=cls.EXPENSE)

    # noinspection PyMethodParameters
    @ClassProperty
    def incomes(cls):
        return cls.query.filter_by(_type=cls.INCOME)
