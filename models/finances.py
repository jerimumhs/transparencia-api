from sqlalchemy.dialects.postgresql import UUID

from models.base import db, BaseModel


class Ticket(BaseModel):
    name = db.Column(db.String(50))
    value = db.Column(db.Float)

    type = db.Column(db.String(10))
    __mapper_args__ = {
        'polymorphic_identity': 'ticket',
        'polymorphic_on': type
    }


class Expense(Ticket):
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('ticket.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'expense',
    }


class Income(Ticket):
    id = db.Column(UUID(as_uuid=True), db.ForeignKey('ticket.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'income',
    }
