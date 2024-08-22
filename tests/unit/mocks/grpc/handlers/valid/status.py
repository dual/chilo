from chilo_api import requirements, Request, Response


@requirements(
    protobuf='messenger.proto',
    service='Messenger',
    rpc='CheckStatus'
)
def check_status(request: Request, response: Response) -> Response:
    sender = request.body.get('sender', '')
    receiver = request.body.get('receiver', '')
    response.body = {
        'success': True,
        'content': f'Message from {sender} to {receiver} successfully sent.'
    }
    return response
