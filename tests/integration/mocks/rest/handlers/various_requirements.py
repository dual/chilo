from chilo_api import requirements


@requirements(
    required_headers=['x-api-key'],
    required_query=['user_type'],
)
def get(_, response):
    response.body = {'various_required_requirements': True}
    return response


@requirements(
    available_query=['first', 'middle', 'last']
)
def delete(_, response):
    response.body = {'various_available_requirements': True}
    return response
