from chilo_api import requirements


@requirements(
    auth_required=True
)
def post(request, response):
    response.body = {'router_directory_basic': request.body}
    return response


@requirements(
    required_headers=['x-api-key'],
    available_headers=['content-type']
)
def get(_, response):
    response.body = {'router_directory_basic': 'GOT'}
    response.headers = ('x-new-header', 'NEW-HEADER')
    return response


def patch(_, response):
    response.body = {'router_directory_basic': 'PATCH'}
    return response


@requirements(
    custom_list=[1, 2, 3],
    custom_dict={'key': 'value'},
    custom_simple=1
)
def put(_, response):
    response.body = {'endpoint_directory_basic': 'put'}
    return response


@requirements(
    required_route='/some/route/{id}'
)
def delete(_, response):
    response.body = {'endpoint_directory_basic': 'delete'}
    return response


@requirements(
    required_response='somme-response-schema'
)
def search(_, response):
    response.body = {'endpoint_directory_basic': 'search'}
    return response
