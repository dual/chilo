from chilo_api.core.requirements import requirements


@requirements(required_route='/bad/dynamic/{id}')
def post(_, response):
    response.body = {'directory_dynamic_bad': True}
    return response


@requirements(required_route='/bad_dynamic/{id')
def get(_, response):
    response.body = {'directory_dynamic_bad': True}
    return response


@requirements()
def patch(_, response):
    response.body = {'directory_dynamic_bad': True}
    return response


@requirements(required_route='/bad-dynamic/{id}')
def delete(_, response):
    response.body = {'directory_dynamic_bad': True}
    return response
