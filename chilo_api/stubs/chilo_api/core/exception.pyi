from _typeshed import Incomplete

class ApiException(Exception):
    code: Incomplete
    key_path: Incomplete
    message: Incomplete
    def __init__(self, **kwargs) -> None: ...

class ApiTimeOutException(Exception):
    code: Incomplete
    key_path: Incomplete
    message: Incomplete
    def __init__(self, **kwargs) -> None: ...
