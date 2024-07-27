from chilo_api import Chilo


api = Chilo(
    base_path='/basic/v1',
    handlers='tests/mocks/handlers/integration-tests',
    port=3000
)
