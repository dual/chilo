from chilo_api import Chilo

startup_events: list[str] = []
shutdown_events: list[str] = []


def on_startup():
    startup_events.append('grpc-started')


def on_shutdown():
    shutdown_events.append('grpc-stopped')


api = Chilo(
    api_type='grpc',
    handlers='tests/integration/mocks/grpc/handlers',
    protobufs='tests/integration/mocks/grpc/protobufs',
    reflection=True,
    port=50051,
    on_startup=[on_startup],
    on_shutdown=[on_shutdown]
)
