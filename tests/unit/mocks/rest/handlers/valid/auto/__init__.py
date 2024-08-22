from chilo_api import requirements


@requirements()
def post(request, response):
    response.body = {'router_directory_auto': request.body}
    return response


@requirements(
    required_response='v1-required-response'
)
def get(_, response):
    response.body = {'page_number': 1, 'bad-data': {'id': '2'}}
    return response


@requirements(
    required_response='v1-required-response'
)
def put(_, response):
    response.body = {'page_number': 1, 'data': {'id': '2'}}
    return response
