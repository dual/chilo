from turtle import st
from chilo_api.core.requirements import requirements


def fail_before(request, response, *args, **kwargs):
    response.set_error('failed before', 'failed')


@requirements(stream=True)
def success(request, response):
    response.body = {'message': 'This is a stream response'}
    yield response


@requirements(stream=True, before=fail_before)
def fail(request, response):
    response.body = {'message': 'This is a stream response'}
    yield response
