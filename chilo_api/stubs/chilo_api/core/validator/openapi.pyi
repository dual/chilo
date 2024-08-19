from _typeshed import Incomplete
from chilo_api.core.resolver.importer import ResolverImporter as ResolverImporter
from chilo_api.core.validator.schema import Schema as Schema

class OpenApiValidator:
    SUPPORTED_METHODS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def validate_openapi(self) -> None: ...
