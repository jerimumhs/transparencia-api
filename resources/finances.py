from loguru import logger
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from models.finances import Ticket
from schemas.finances import ticket_schema, tickets_schema


class TicketList(Resource):
    @logger.catch
    def get(self):
        return tickets_schema.dump(Ticket.query.all())

    @logger.catch
    def post(self):
        try:
            ticket = ticket_schema.load(request.get_json())
            ticket.save()
            return ticket_schema.dump(ticket), 200
        except ValidationError as e:
            return e.messages, 400
        except Exception as e:
            return e.__str__(), 400


class TicketDetail(Resource):
    @logger.catch
    def get(self, ticket_id):
        pass

    @logger.catch
    def put(self, ticket_id):
        try:
            ticket = Ticket.query.filter_by(id=ticket_id).one()
            ticket = ticket_schema.load(request.get_json(), instance=ticket)
            ticket.save()
            return ticket_schema.dump(ticket), 200
        except ValidationError as e:
            return e.messages, 400
        except NoResultFound:
            return f"Ticket não encontrado com o id {ticket_id}!", 404
        except Exception as e:
            return e.__str__(), 500

    @logger.catch
    def delete(self, ticket_id):
        pass
