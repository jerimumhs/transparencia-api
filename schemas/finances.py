from marshmallow import fields, validates, ValidationError

from app import ma, db
from models.finances import Ticket


class TicketSchema(ma.ModelSchema):
    class Meta:
        model = Ticket
        session = db.session
        fields = ['title', 'description', 'date', 'value', 'type', 'type_name']

    type_name = fields.String(attribute='_type.name', dump_only=True)

    @validates("type")
    def validate_type(self, value):
        try:
            Ticket.TicketType(value)
        except ValueError as e:
            raise ValidationError(f'{e}') from e


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
