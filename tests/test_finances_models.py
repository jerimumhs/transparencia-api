from tests import BaseTestCase
from models.finances import Ticket
from tests.factories.finances import TicketFactory


class TestTicket(BaseTestCase):
    def test_create_ticket(self):
        self.assertEqual(Ticket.query.count(), 0)
        TicketFactory()
        self.assertEqual(Ticket.query.count(), 1)

    def test_create_ticket_empty_description(self):
        self.assertEqual(Ticket.query.count(), 0)
        TicketFactory(description='')
        self.assertEqual(Ticket.query.count(), 1)

    def test_create_ticket_fail(self):
        self.assertEqual(Ticket.query.count(), 0)
        self.assertRaises(ValueError, TicketFactory, title='')
        self.assertRaises(ValueError, TicketFactory, title=None)
        self.assertRaises(ValueError, TicketFactory, date=None)
        self.assertRaises(ValueError, TicketFactory, value=None)
        self.assertRaises(ValueError, TicketFactory, value=0)
        self.assertRaises(ValueError, TicketFactory, value=-1)
        self.assertRaises(ValueError, TicketFactory, type='')
        self.assertRaises(ValueError, TicketFactory, type='TEASER')
        self.assertEqual(Ticket.query.count(), 0)

    def test_create_income(self):
        self.assertEqual(Ticket.query.count(), 0)
        TicketFactory(type=Ticket.TicketType.INCOME)
        self.assertEqual(Ticket.query.count(), 1)
        self.assertEqual(Ticket.incomes.count(), 1)
        self.assertEqual(Ticket.expenses.count(), 0)

    def test_create_expense(self):
        self.assertEqual(Ticket.query.count(), 0)
        TicketFactory(type=Ticket.TicketType.EXPENSE)
        self.assertEqual(Ticket.query.count(), 1)
        self.assertEqual(Ticket.expenses.count(), 1)
        self.assertEqual(Ticket.incomes.count(), 0)
