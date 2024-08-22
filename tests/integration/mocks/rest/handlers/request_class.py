from chilo_api import requirements


class TestRequestClass:
    def __init__(self, request):
        self.request = request
        self.initialized = True


@requirements(request_class=TestRequestClass)
def get(test_class, response):
    response.body = {'request_class': test_class.initialized}
    return response
