from chilo_api.core.exception import ApiException as ApiException, ApiTimeOutException as ApiTimeOutException
from chilo_api.core.json_helper import JsonHelper as JsonHelper
from chilo_api.core.logger.common import CommonLogger as CommonLogger
from chilo_api.core.request import Request as Request
from chilo_api.core.resolver import Resolver as Resolver
from chilo_api.core.response import Response as Response
from chilo_api.core.types.router_settings import RouterSettings as RouterSettings
from chilo_api.core.validator import Validator as Validator
from chilo_api.core.validator.config import ConfigValidator as ConfigValidator
from typing_extensions import Unpack

class Router:
    def __init__(self, **kwargs: Unpack[RouterSettings]) -> None: ...
    @property
    def handlers(self): ...
    @property
    def base_path(self): ...
    @property
    def host(self): ...
    @property
    def port(self): ...
    @property
    def reload(self): ...
    @property
    def verbose(self): ...
    @property
    def timeout(self): ...
    @property
    def openapi_validate_request(self): ...
    @property
    def openapi_validate_response(self): ...
    def route(self, environ, server_response): ...