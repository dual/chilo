def get(_, response):
    response.body = {'hello': 'nested'}
    return response