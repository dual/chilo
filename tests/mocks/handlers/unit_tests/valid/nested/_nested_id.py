from chilo_api.core.requirements import requirements


@requirements(
    required_headers=['content-type'],
    required_route='/nested/{nested_id}',
    required_body='v1-patch-request-test'
)
def patch(request, response):
    response.body = {'router_nested_directory_dynamic': request.body, 'path_params': request.path_params}
    return response
