def get(_, response):
    response.body = {'hello': 'triple'}
    return response