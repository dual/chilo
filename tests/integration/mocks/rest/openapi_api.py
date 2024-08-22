from chilo_api import Chilo


def auth(request, response, _):
    if not request.headers.get('x-api-key'):
        response.code = 401
        response.set_error('headers', 'unauthorized access')


def before_all(request, response, _):
    # This is a placeholder for before_all logic
    pass


def after_all(request, response, _):
    # This is a placeholder for after_all logic
    pass


api = Chilo(  # type: ignore[call-arg]
    base_path='/basic/v1',
    handlers='tests/integration/mocks/rest/handlers',
    openapi='tests/unit/mocks/openapi/variations/openapi-integration-tests.yml',
    openapi_validate_request=True,
    openapi_validate_response=True,
    before_all=before_all,
    when_auth_required=auth,
    after_all=after_all,
    cors=True,
    port=3000
)
