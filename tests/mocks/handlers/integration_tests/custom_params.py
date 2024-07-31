from chilo_api import requirements


def before_get(request, response, requirements):
    permission_header = request.headers.get('x-user-role')
    if not permission_header or permission_header != requirements['permissions']:
        response.code = 401
        response.set_error('permission', 'must be admin to access data')
        return response


@requirements(before=before_get, permissions='admin')
def get(_, response):
    response.body = {'custom_params': True}
    return response
