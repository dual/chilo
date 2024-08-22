from typing import List

from chilo_api import requirements
from pydantic import BaseModel, PositiveInt


@requirements(required_body='v1-post-required-body')
def post(_, response):
    response.body = {'post_required_body_string': True}
    return response


@requirements(required_body={
    'type': 'object',
    'required': ['id'],
    'additionalProperties': False,
    'properties': {
        'id': {
            'type': 'integer'
        },
        'body': {
            'type': 'object'
        },
        'dict': {
            'type': 'boolean'
        }
    }
}
)
def patch(_, response):
    response.body = {'patch_required_body_dict': True}
    return response


class UserRequest(BaseModel):
    id: PositiveInt
    email: str
    active: bool
    favorites: List[str]
    notification_config: dict[str, bool]


@requirements(required_body=UserRequest)
def put(_, response):
    response.body = {'put_required_body_pydantic': True}
    return response
