class HandlerScanner:
    def __init__(self, handlers) -> None: ...
    @property
    def file_separator(self): ...
    @property
    def handlers(self): ...
    @property
    def handlers_base(self): ...
    def clean_path(self, dirty_path): ...
    def get_handler_file_paths(self): ...
