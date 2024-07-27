from chilo_api.core.requirements import requirements


@requirements()
def post(request, response):
    response.body = {'form': request.form, 'headers': request.headers}
    return response


@requirements()
def get(_, response):
    response.body = {'router_directory_basic': 'GOT'}
    response.headers = ('x-new-header', 'NEW-HEADER')
    return response
