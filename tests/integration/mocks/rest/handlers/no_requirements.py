def get(_, response):
    response.body = {'no_requirements': True}
    return response
