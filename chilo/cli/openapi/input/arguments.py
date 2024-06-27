class InputArguments:

    def __init__(self, args):
        self.__base = args.base
        self.__handlers = args.handlers
        self.__output = args.output or args.handlers
        self.__formats = args.format or 'yml'
        self.__delete = args.delete or False

    @property
    def base(self):
        return self.__base

    @property
    def handlers(self):
        return self.__handlers

    @property
    def output(self):
        return self.__output

    @property
    def formats(self):
        return self.__formats.split(',')

    @property
    def delete(self):
        return self.__delete
