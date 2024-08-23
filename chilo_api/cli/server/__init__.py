from werkzeug.serving import run_simple


from chilo_api.cli.server.arguments import ServerArguments
from chilo_api.cli.server.importer import ServerImporter
from chilo_api.cli.server.logger import ServerLogger
from chilo_api.cli.server.validator import ServerValidator

from chilo_api.cli.grpc import import_rpc_funcs


def __start_server(server):
    run_simple(
        server.host,
        server.port,
        server.route,
        use_reloader=server.reload,
        use_debugger=server.verbose
    )


def __run_rest_server(validaitor, server):
    validaitor.validate(server)
    __start_server(server)


def __run_grpc_server(server):
    rpc_funcs = import_rpc_funcs(server)
    print(rpc_funcs)
    # 1. scan all handlers looking for rpc_* functions
        # 1a. [if rpc] capture the file name, function name, protobuf kwarg in requirements
        # 1b. [for every unique protobuf file] generate code using the command-line


def __get_server(args):
    importer = ServerImporter(args.api)
    api = importer.get_api_module()
    return ServerArguments(args, api)


def run_server(args):
    validaitor = ServerValidator()
    logger = ServerLogger()

    logger.log_start()
    logger.log_logo()

    server = __get_server(args)
    logger.log_settings(server)
    if server.api_type == 'grpc':
        __run_grpc_server(server)
    else:
        __run_rest_server(validaitor, server)
