import abc
from typing import Any, Optional

from chilo_api.core.placeholders.grpc import GRPCContextPlaceHolder


class ResponseInterface(abc.ABC):
    '''
    An interface for response handling classes.
    This interface defines the methods and properties that any response handling class must implement.
    '''

    def __init__(self):
        self._code: int = 200  # NOSONAR Overwrite WSGI behavior for gRPC context
        self._body: Optional[Any] = None
        self._has_errors: bool = False

    @property
    @abc.abstractmethod
    def body(self) -> Any:
        pass

    @body.setter
    @abc.abstractmethod
    def body(self, body: Any) -> None:
        pass

    @property
    @abc.abstractmethod
    def code(self) -> int:
        pass

    @code.setter
    @abc.abstractmethod
    def code(self, code: int) -> None:
        pass

    @property
    @abc.abstractmethod
    def has_errors(self) -> bool:
        pass

    @abc.abstractmethod
    def set_error(self, key_path: str, message: str) -> None:
        pass

    @abc.abstractmethod
    def get_response(self) -> Any:
        pass
