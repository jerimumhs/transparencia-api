from marshmallow import fields

from app import ma, db
from models.finances import Ticket


class TicketSchema(ma.ModelSchema):
    type_name = fields.String(attribute='_type.name', dump_only=True)

    class Meta:
        model = Ticket
        session = db.session
        fields = ['name', 'date', 'value', 'type', 'type_name']
