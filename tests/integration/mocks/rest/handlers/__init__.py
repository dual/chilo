def get(_, response):
    response.body = {'hello': True}
    return response
