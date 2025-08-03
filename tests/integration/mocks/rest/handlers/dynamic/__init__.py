from chilo_api import requirements


@requirements()
def get(_, response):
    response.body = {'dynamic': True}
    return response
