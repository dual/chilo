from chilo_api import requirements


@requirements(
    required_route='/dynamic/{dynamic_id}'
)
def get(request, response):
    response.body = {'dynamic_id': request.path_params['dynamic_id']}
    return response


@requirements(
    required_route='/dynamic/{dynamic_id}/{some_var}/{last_var}'
)
def delete(request, response):
    response.body = {
        'dynamic_id': request.path_params['dynamic_id'],
        'some_var': request.path_params['some_var'],
        'last_var': request.path_params['last_var']
    }
    return response
