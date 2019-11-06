import datetime

from tests import BaseTestCase
from models.finances import Ticket
from schemas.finances import TicketSchema
from tests.factories.finances import TicketFactory


class TestFinances(BaseTestCase):
    def test_ticket_dump(self):
        self.assertEqual(Ticket.query.count(), 0)
        ticket = TicketFactory(name='test', date=datetime.date(2019, 1, 1), type=Ticket.TicketType.INCOME, value=10)
        self.assertEqual(Ticket.query.count(), 1)
        schema = TicketSchema()
        data = schema.dump(ticket)
        self.assertIsInstance(data, dict)
        self.assertEqual(data, {
            'name': 'test', 'date': '2019-01-01',
            'value': 10.0, 'type': 2, 'type_name': 'INCOME'
        })

    def test_ticket_load(self):
        data = {
            'name': 'test', 'date': '2019-01-01',
            'value': 10.0, 'type': 2
        }
        schema = TicketSchema()
        self.assertEqual(Ticket.query.count(), 0)
        schema.load(data).save()
        self.assertEqual(Ticket.query.count(), 1)

    def test_ticket_load_instance(self):
        self.assertEqual(Ticket.query.count(), 0)
        ticket = TicketFactory(name='original')
        self.assertEqual(Ticket.query.count(), 1)

        data = {
            'name': 'test', 'date': '2019-01-01',
            'value': 10.0, 'type': 2
        }
        schema = TicketSchema()
        schema.load(data, instance=ticket).save()
        self.assertEqual(Ticket.query.first().name, 'test')
