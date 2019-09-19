from flask_restful import Resource
from loguru import logger


class ServerStatus(Resource):
    @logger.catch
    def get(self):
        return {'status': 'I\'m fine, thanks.'}, 200


def add_resources(api):
    api.add_resource(
        ServerStatus,
        '/status/'
    )
