from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    handlers='tests/integration/mocks/grpc/handlers',
    protobufs='tests/integration/mocks/grpc/protobufs',
    reflection=True,
    port=50051
)
