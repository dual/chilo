from typing import Generator
from chilo_api import requirements, Request, Response


@requirements(
    protobuf='streamer.proto',
    service='Streamer',
    rpc='Stream',
    stream=True
)
def stream(request: Request, response: Response) -> Generator[Response, None, None]:
    for query in request.body:
        response_msg = response.rpc_response() # type: ignore
        response_msg.results = f"Received: {query.query}"
        yield response_msg
