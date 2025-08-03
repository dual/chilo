from chilo_api import requirements, Request, Response


@requirements(
    protobuf='messenger.proto',
    service='Messenger',
    rpc='SendMessage'
)
def send_message(request: Request, response: Response) -> Response:
    sender = request.body.get('sender', '')
    receiver = request.body.get('receiver', '')
    content = request.body.get('content', '')
    response.body = {
        'success': True,
        'content': f'Message from {sender} to {receiver}: {content}'
    }
    return response
