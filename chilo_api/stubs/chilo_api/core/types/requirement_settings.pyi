from typing import Any, Callable, TypedDict

class RequirementSettings(TypedDict):
    required_headers: list[str] | None
    available_headers: list[str] | None
    required_query: list[str] | None
    available_query: list[str] | None
    required_body: Any | None
    required_path: str | None
    required_response: Any | None
    auth_required: bool | None
    before: Callable | None
    after: Callable | None
    request_class: Any | None
    timeout: int | None
    custom: Any | None
    summary: str | None
    deprecated: bool | None
