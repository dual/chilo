class GRPCContextPlaceHolder:
    '''
    A placeholder class for gRPC context to avoid errors when context is not provided.
    '''

    def __getattr__(self, name: str) -> None:
        '''
        Called when an attribute is not found.
        Returns None for any non-existent attribute.
        '''
        print(f'Warning: Attempted to access non-existent attribute "{name}". Returning None.')  # pragma: no cover
