from chilo_api import requirements


def before_post(request, response, requirements):
    request.context = ['before_post']


def after_post(request, response, requirements):
    request.context.append('after_post')
    body = response.raw
    body['call_order'] = request.context
    response.body = body


@requirements(before=before_post, after=after_post)
def post(_, response):
    response.body = {'before_after': True}
    return response
