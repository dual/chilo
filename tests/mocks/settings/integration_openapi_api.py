from chilo_api import Chilo


api = Chilo(
    base_path='/openapi/v1',
    handlers='tests/mocks/handlers/integration-tests',
    openapi='tests/mocks/openapi/variations/openapi.yml',
    openapi_validate_request=True,
    openapi_validate_response=True,
    port=3001
)
