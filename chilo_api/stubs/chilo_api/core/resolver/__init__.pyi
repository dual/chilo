from chilo_api.core.endpoint import Endpoint as Endpoint
from chilo_api.core.exception import ApiException as ApiException
from chilo_api.core.resolver.cache import ResolverCache as ResolverCache
from chilo_api.core.resolver.scanner import ResolverScanner as ResolverScanner

class Resolver:
    def __init__(self, **kwargs) -> None: ...
    @property
    def cache_misses(self): ...
    def auto_load(self) -> None: ...
    def reset(self) -> None: ...
    def get_endpoint(self, request): ...
