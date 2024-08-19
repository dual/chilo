from _typeshed import Incomplete
from chilo_api.core.exception import ApiException as ApiException
from chilo_api.core.resolver.importer import ResolverImporter as ResolverImporter

class ResolverScanner:
    importer: Incomplete
    base_path: Incomplete
    has_dynamic_route: bool
    file_tree_climbed: bool
    dynamic_parts: Incomplete
    import_path: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def load_importer_files(self) -> None: ...
    def get_endpoint_module(self, request): ...
