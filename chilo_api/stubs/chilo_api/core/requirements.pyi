from chilo_api.core.exception import ApiTimeOutException as ApiTimeOutException
from chilo_api.core.request import Request as Request
from chilo_api.core.response import Response as Response
from chilo_api.core.types.requirement_settings import RequirementSettings as RequirementSettings
from typing_extensions import Unpack

def requirements(**kwargs: Unpack[RequirementSettings]): ...
