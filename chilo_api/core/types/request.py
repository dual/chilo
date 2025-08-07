from typing import TypeVar, Union

from chilo_api.core.rest.request import RestRequest
from chilo_api.core.grpc.request import GRPCRequest

Request = TypeVar('Request', bound=Union[RestRequest, GRPCRequest])
