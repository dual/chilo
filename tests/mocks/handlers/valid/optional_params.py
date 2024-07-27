from chilo_api.core.requirements import requirements


@requirements()
def get(_, response):
    response.body = {'router_directory_optional': True}
    return response
