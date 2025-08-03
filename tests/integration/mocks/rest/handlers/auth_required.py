from chilo_api import requirements


@requirements(auth_required=True)
def get(_, response):
    response.body = {'auth_passed': True}
    return response
