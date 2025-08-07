from typing import TypeVar, Union

from chilo_api.core.rest.response import RestResponse
from chilo_api.core.grpc.response import GRPCResponse

Response = TypeVar('Response', bound=Union[RestResponse, GRPCResponse])
