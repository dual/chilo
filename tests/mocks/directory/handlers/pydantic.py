from chilo.core.requirements import requirements

from tests.mocks.common.mock_pydantic_class import UserRequest


@requirements(required_body=UserRequest)
def post(_, response):
    response.body = {'pydantic_pass': True}
    return response