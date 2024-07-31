from chilo_api import Chilo


def auth(request, response, _):
    if not request.headers.get('x-api-key'):
        response.code = 401
        response.set_error('headers', 'unauthorized access')


def before_all(request, response, _):
    pass


def after_all(request, response, _):
    pass


api = Chilo(
    base_path='/basic/v1',
    handlers='tests/mocks/handlers/integration_tests',
    openapi='tests/mocks/openapi/variations/openapi-integration-tests.yml',
    openapi_validate_spec=False,
    before_all=before_all,
    when_auth_required=auth,
    after_all=after_all,
    port=3000
)
