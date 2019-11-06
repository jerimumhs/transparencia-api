from flask_restful import Resource
from loguru import logger


class ServerStatus(Resource):
    @logger.catch
    def get(self):
        """
        get endpoint
        ---
        tags:
          - Status
        responses:
          200:
            description: The api is up
        """
        return {'status': 'I\'m fine, thanks.'}, 200
