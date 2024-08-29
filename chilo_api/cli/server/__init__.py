from werkzeug.serving import run_simple


from chilo_api.cli.server.arguments import ServerArguments
from chilo_api.cli.server.importer import ServerImporter
from chilo_api.cli.server.logger import ServerLogger
from chilo_api.cli.server.validator import ServerValidator

from chilo_api.cli.grpc import run_grpc_simple


def __run_rest_server(server):
    run_simple(
        server.host,
        server.port,
        server.route,
        use_reloader=server.reload,
        use_debugger=server.verbose
    )


def __run_grpc_server(server):
    run_grpc_simple(server)


def run_server(args):
    validaitor = ServerValidator()
    logger = ServerLogger()

    logger.log_start()
    logger.log_logo()

    importer = ServerImporter(args.api)
    api = importer.get_api_module()
    server = ServerArguments(args, api)
    logger.log_settings(server)

    validaitor.validate(server)
    if server.api_type == 'grpc':
        __run_grpc_server(server)
    else:
        __run_rest_server(server)
