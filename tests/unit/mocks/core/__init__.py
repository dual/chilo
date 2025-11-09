class HookTracker:
    """Records how many times hooks run."""

    def __init__(self) -> None:
        self.calls = []

    def hook(self, label) -> None:
        self.calls.append(label)

    def __call__(self, label=None):
        if label is None:
            label = f'hook-{len(self.calls)+1}'
        self.hook(label)

    def reset(self) -> None:
        self.calls.clear()


class FailingHook:
    """Callable that raises a provided exception."""

    def __init__(self, exception: Exception) -> None:
        self.exception = exception

    def __call__(self) -> None:
        raise self.exception
