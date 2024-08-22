import time

from chilo_api.core.requirements import requirements


call_order = []


class TestRequestClass:
    def __init__(self, request):
        self.request = request
        self.initialized = True


def fail_before(request, response, *args, **kwargs):
    response.set_error('failed before', 'failed')


def before_call(request, response, reqs):
    before_call.has_been_called = True  # type: ignore
    global call_order
    call_order.append('before')


def after_call(request, response, reqs):
    after_call.has_been_called = True  # type: ignore
    global call_order
    call_order.append('after')


@requirements(
    custom_requiremnent=True,
    before=before_call,
    after=after_call,
    request_class=TestRequestClass
)
def post(request_class, response):
    response.body = {'requirements_basic': request_class.initialized}
    return response


@requirements()
def get(_, response):
    time.sleep(2)
    response.body = {'timeout_basic': 'timeout'}
    return response


@requirements(timeout=1)
def patch(_, response):
    time.sleep(2)
    response.body = {'timeout_basic': 'timeout'}
    return response

