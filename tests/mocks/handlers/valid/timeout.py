import time

from chilo_api.core.requirements import requirements


@requirements()
def post(request, response):
    time.sleep(5)
    response.body = {'router_directory_basic_timeout': request.body}
    return response


@requirements(timeout=1)
def get(request, response):
    time.sleep(5)
    response.body = {'router_directory_basic_timeout': request.body}
    return response
