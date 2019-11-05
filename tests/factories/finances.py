from factory import Faker

from models.finances import Ticket
from tests.factories import BaseModelFactory


class TicketFactory(BaseModelFactory):
    class Meta:
        model = Ticket

    name = Faker('text', max_nb_chars=14)
    value = Faker('pyfloat', positive=True,
                  right_digits=2, max_value=100, min_value=1)
    date = Faker('date_this_year')
    type = Faker('random_element', elements=Ticket.TicketType)
