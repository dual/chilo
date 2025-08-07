import abc
from typing import Any

from chilo_api.core.interfaces.wsgi import GRPCWSGIPlaceHolder


class RequestInterface(abc.ABC):
    '''
    An interface for request handling classes.
    This interface defines the methods and properties that any request handling class must implement.
    '''

    def __init__(self, **kwargs):
        self._wsgi = kwargs.get('wsgi', GRPCWSGIPlaceHolder())
        self._context = {}

    @property
    @abc.abstractmethod
    def api_type(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def body(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def json(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def raw(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def context(self) -> Any:
        pass

    @context.setter
    @abc.abstractmethod
    def context(self, context: Any) -> None:
        pass
