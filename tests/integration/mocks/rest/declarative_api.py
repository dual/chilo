from chilo_api import Chilo

startup_events: list[str] = []
shutdown_events: list[str] = []


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


def on_startup():
    startup_events.append('rest-started')


def on_shutdown():
    shutdown_events.append('rest-stopped')


api = Chilo(
    base_path='/basic/v1',
    handlers='tests/integration/mocks/rest/handlers',
    openapi='tests/unit/mocks/openapi/variations/openapi-integration-tests.yml',
    openapi_validate_spec=False,
    before_all=before_all,
    when_auth_required=auth,
    after_all=after_all,
    cors=True,
    port=3000,
    on_startup=[on_startup],
    on_shutdown=[on_shutdown]
)
