import datetime

from marshmallow.exceptions import ValidationError

from tests import BaseAPITestCase, BaseTestCase
from models.finances import Ticket
from schemas.finances import ticket_schema
from tests.factories.finances import TicketFactory


class TestTicketResources(BaseTestCase):
    # def setUp(self):
    #     super(TestTicketResources, self).setUp()
    #     self.endpoint = 'tickets'

    def test_create_ticket(self):
        self.assertEqual(Ticket.query.count(), 0)

        data = {
            'title': 'teste',
            'value': 10.0,
            'date': '2019-01-01',
            'type': Ticket.TicketType.INCOME.value
        }

        # path = self.get_path()
        response = self.client.post('tickets/', json=data)

        self.assertEqual(response.status_code, 200, msg=response.data)
        self.assertEqual(Ticket.query.count(), 1)

    def test_create_ticket_fail(self):
        self.assertEqual(Ticket.query.count(), 0, msg=ticket_schema.dump(Ticket.query.first()))

        data = {
            'title': 1,
            'value': 'a',
            'date': '201-01',
            'type': 'a'
        }

        # path = self.get_path()
        response = self.client.post('tickets/', json=data)

        self.assertEqual(response.status_code, 400, msg=response.data)
        self.assertTrue(response.json.get('title'))
        self.assertTrue(response.json.get('value'))
        self.assertTrue(response.json.get('date'))
        self.assertTrue(response.json.get('type'))
        self.assertEqual(Ticket.query.count(), 0, msg=ticket_schema.dump(Ticket.query.first()))
