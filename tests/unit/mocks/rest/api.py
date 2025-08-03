from chilo_api import Chilo


api = Chilo(  # type: ignore[call-arg]
    base_path='/',
    handlers='tests/unit/mocks/rest/handlers/valid',
    cors=True
)
