from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    protobufs='tests/mocks/grpc/unit_tests/protobufs',
    handlers='tests/mocks/grpc/unit_tests/handlers'
)
