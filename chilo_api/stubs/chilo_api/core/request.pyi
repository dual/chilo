from chilo_api.core import logger as logger
from chilo_api.core.json_helper import JsonHelper as JsonHelper
from typing import Any

class Request:
    def __init__(self, **kwargs) -> None: ...
    @property
    def wsgi(self) -> Any: ...
    @property
    def authorization(self) -> dict: ...
    @property
    def cookies(self) -> dict: ...
    @property
    def protocol(self) -> str: ...
    @property
    def content_type(self) -> str: ...
    @property
    def mimetype(self) -> str: ...
    @property
    def host_url(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def method(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def route(self) -> str: ...
    @route.setter
    def route(self, route: str): ...
    @property
    def headers(self) -> dict: ...
    @property
    def body(self) -> Any: ...
    @property
    def json(self) -> dict: ...
    @property
    def form(self) -> dict: ...
    @property
    def xml(self) -> dict: ...
    @property
    def files(self) -> dict: ...
    @property
    def graphql(self) -> dict: ...
    @property
    def raw(self) -> Any: ...
    @property
    def query_params(self) -> dict: ...
    @property
    def path_params(self) -> dict: ...
    @path_params.setter
    def path_params(self, path_params: tuple): ...
    @property
    def context(self) -> Any: ...
    @context.setter
    def context(self, context: Any): ...
    @property
    def timeout(self) -> int: ...
    def clear_path_params(self) -> None: ...
