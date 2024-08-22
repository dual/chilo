from chilo_api import requirements


@requirements()
def get(_, response):
    response.body = {'router_pattern_dyamic_basic': 'GOT'}
    response.headers = ('x-new-header', 'NEW-HEADER')
    return response
