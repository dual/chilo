def get(_, response):
    response.body = {'hello': 'user'}
    return response