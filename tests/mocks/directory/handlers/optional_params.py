from chilo.core.requirements import requirements


@requirements()
def get(request, response):
    response.body = {'router_directory_optional': True}
    return response
