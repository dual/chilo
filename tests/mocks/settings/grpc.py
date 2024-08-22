from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    protobufs='tests/mocks/grpc/protobufs',
    handlers='tests/mocks/grpc/handlers',
)
