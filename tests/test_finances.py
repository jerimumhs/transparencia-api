from tests import BaseTestCase
from models.finances import Ticket, Income, Expense


class TestFinances(BaseTestCase):
    def test_ticket(self):
        self.assertEqual(Ticket.query.count(), 0)
        Ticket(name='Teste', value=10.50).save()
        self.assertEqual(Ticket.query.count(), 1)
        self.assertEqual(Ticket.query.first().name, 'Teste')

    def test_income(self):
        self.assertEqual(Income.query.count(), 0)
        Income(name='Teste', value=10.50).save()
        self.assertEqual(Income.query.count(), 1)
        self.assertEqual(Income.query.first().name, 'Teste')

    def test_expense(self):
        self.assertEqual(Expense.query.count(), 0)
        Expense(name='Teste', value=10.50).save()
        self.assertEqual(Expense.query.count(), 1)
        self.assertEqual(Expense.query.first().name, 'Teste')
