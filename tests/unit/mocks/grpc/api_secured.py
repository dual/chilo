from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    handlers='tests/unit/mocks/grpc/handlers/valid',
    protobufs='tests/unit/mocks/grpc/protobufs',
    private_key='tests/unit/mocks/grpc/server.key',
    certificate='tests/unit/mocks/grpc/server.crt',
    port=50051
)
