from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    handlers='tests/unit/mocks/grpc/handlers/valid',
    protobufs='tests/unit/mocks/grpc/protobufs',
    reflection=True,
    port=50051
)
