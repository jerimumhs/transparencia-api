from tests import BaseTestCase
from models.finances import Ticket


class TestExpenses(BaseTestCase):
    def test_ticket(self):
        self.assertEqual(Ticket.query.count(), 0)
        Ticket(name='Teste', value=10.50).save()
        self.assertEqual(Ticket.query.count(), 1)
        self.assertEqual(Ticket.query.first().name, 'Teste')
