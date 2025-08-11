import time
from typing import Generator
from chilo_api import requirements, Request, Response

@requirements(
    protobuf='streamer.proto',
    service='Streamer',
    rpc='BiStream',
    stream_response=True
)
def bi_stream(request: Request, response: Response) -> Generator[Response, None, None]:
    for query in request.body:
        response_msg = response.rpc_response()  # type: ignore
        response_msg.results = f"Received: {query.query}"
        yield response_msg


@requirements(
    protobuf='streamer.proto',
    service='Streamer',
    rpc='ClientStream',
)
def client_stream(request: Request, response: Response) -> Response:
    total = 0
    for request in request.body:
        total += 1
    response.body = {'results': f"Total requests received: {total}"}
    return response


@requirements(
    protobuf='streamer.proto',
    service='Streamer',
    rpc='ServerStream',
    stream_response=True
)
def server_stream(request: Request, response: Response) -> Generator[Response, None, None]:
    for i in range(5):
        time.sleep(0.5)  # Simulate processing delay
        response_msg = response.rpc_response()  # type: ignore
        response_msg.results = f"Server Stream Response {i + 1} for query: {request.body['query']}"
        yield response_msg
