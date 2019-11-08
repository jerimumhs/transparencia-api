from resources.status import ServerStatus
from resources.finances import TicketList, TicketDetail


def add_resources(api):
    api.add_resource(
        ServerStatus,
        '/status/'
    )
    api.add_resource(
        TicketList,
        '/tickets/'
    )
    api.add_resource(
        TicketDetail,
        '/tickets/<ticket_id>'
    )
