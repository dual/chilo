from chilo_api.core.requirements import requirements


def fail_before(request, response, *args, **kwargs):
    response.set_error('failed before', 'failed')


@requirements(before=fail_before)
def delete(_, response):
    response.body = {'fail': True}
    return response
