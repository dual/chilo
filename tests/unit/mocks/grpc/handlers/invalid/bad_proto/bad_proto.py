from chilo_api import requirements, Request, Response


@requirements(
    protobuf='bad.proto',
    service='Bad',
    rpc='Proto'
)
def add(request: Request, response: Response) -> Response:
    num1 = request.body.get('num1', 0)
    num2 = request.body.get('num2', 0)
    result = num1 + num2
    response.body = {'result': result}
    return response
