import datetime

from marshmallow.exceptions import ValidationError

from tests import BaseTestCase
from models.finances import Ticket
from schemas.finances import ticket_schema
from tests.factories.finances import TicketFactory


class TestTicketResources(BaseTestCase):
    def test_ticket_dump(self):
        self.assertEqual(Ticket.query.count(), 0)
        ticket = TicketFactory(title='test', description='desc', date=datetime.date(2019, 1, 1), type=Ticket.TicketType.INCOME, value=10)
        self.assertEqual(Ticket.query.count(), 1)
        data = ticket_schema.dump(ticket)
        self.assertIsInstance(data, dict)
        self.assertEqual(data, {
            'title': 'test', 'description': 'desc', 'date': '2019-01-01',
            'value': 10.0, 'type': 2, 'type_name': 'INCOME'
        })

    def test_ticket_load(self):
        data = {
            'title': 'test', 'description': 'desc', 'date': '2019-01-01',
            'value': 10.0, 'type': 2
        }
        self.assertEqual(Ticket.query.count(), 0)
        ticket_schema.load(data).save()
        self.assertEqual(Ticket.query.count(), 1)

    def test_ticket_load_missing(self):
        data = {
            'title': 'test',
            'value': 10.0, 'type': 2
        }
        self.assertEqual(Ticket.query.count(), 0)
        self.assertRaises(ValidationError, ticket_schema.load, data)
        self.assertEqual(Ticket.query.count(), 0)

    def test_ticket_load_instance(self):
        self.assertEqual(Ticket.query.count(), 0)
        ticket = TicketFactory(title='original', description='original')
        self.assertEqual(Ticket.query.count(), 1)

        data = {
            'title': 'test', 'date': '2019-01-01',
            'value': 10.0, 'type': 2
        }

        ticket_schema.load(data, instance=ticket).save()
        self.assertEqual(Ticket.query.first().title, 'test')
        self.assertEqual(Ticket.query.first().description, 'original')
