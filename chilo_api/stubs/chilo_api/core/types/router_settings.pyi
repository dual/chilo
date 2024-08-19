from enum import Enum
from typing import Callable, TypedDict

class Cache(Enum):
    ALL = 'all'
    STATIC = 'static-only'
    DYNAMIC = 'dynamic-only'

class RouterSettings(TypedDict):
    handlers: str
    base_path: str
    host: str
    port: int
    reload: bool
    verbose: bool
    before_all: Callable | None
    after_all: Callable | None
    when_auth_required: Callable | None
    on_error: Callable | None
    on_timeout: Callable | None
    cors: bool
    cache_size: int | None
    cache_mode: Cache
    timeout: int | None
    output_error: bool
    openapi: str | None
    openapi_validate_request: bool
    openapi_validate_response: bool
