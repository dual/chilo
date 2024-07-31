from chilo_api.core.requirements import requirements

from tests.mocks.common.pydantic_class import UserRequest

response_schema = {
    'type': 'object',
    'required': ['id', 'body'],
    'additionalProperties': False,
    'properties': {
        'id': {
            'type': 'string'
        },
        'body': {
            'type': 'object'
        },
        'dict': {
            'type': 'boolean'
        }
    }
}


@requirements(required_body=UserRequest)
def post(_, response):
    response.body = {'pydantic_pass': True}
    return response


@requirements(
    required_response=response_schema
)
def put(_, response):
    response.body = {'id': 1, 'body': {'id': '2'}}
    return response
