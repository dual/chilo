from chilo_api import requirements, Request, Response


@requirements(
    protobuf='calculator.proto',
    service='Calculator',
    rpc='Add'
)
def add(request: Request, response: Response) -> Response:
    num1 = request.body.get('num1', 0)
    num2 = request.body.get('num2', 0)
    result = num1 + num2
    response.body = {'result': result}
    return response


@requirements(
    protobuf='calculator.proto',
    service='Calculator',
    rpc='Subtract'
)
def subtract(request: Request, response: Response) -> Response:
    num1 = request.body.get('num1', 0)
    num2 = request.body.get('num2', 0)
    result = num1 - num2
    response.body = {'result': result}
    return response


@requirements(
    protobuf='calculator.proto',
    service='Calculator',
    rpc='Multiply'
)
def multiply(request: Request, response: Response) -> Response:
    num1 = request.body.get('num1', 0)
    num2 = request.body.get('num2', 0)
    result = num1 * num2
    response.body = {'result': result}
    return response


@requirements(
    protobuf='calculator.proto',
    service='Calculator',
    rpc='Divide'
)
def divide(request: Request, response: Response) -> Response:
    num1 = request.body.get('num1', 0)
    num2 = request.body.get('num2', 0)
    if num2 == 0:
        response.set_error(key_path='divide', message='Division by zero is not allowed')
    else:
        result = num1 / num2
        response.body = {'result': result}
    return response
