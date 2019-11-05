from resources.status import ServerStatus


def add_resources(api):
    api.add_resource(
        ServerStatus,
        '/status/'
    )
