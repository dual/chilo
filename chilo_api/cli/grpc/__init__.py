from concurrent import futures
import grpc

from chilo_api.cli.grpc.commander import GRPCCommander
from chilo_api.cli.grpc.endpoint import GRPCEndpoint
from chilo_api.cli.grpc.importer import GRPCImporter
from chilo_api.cli.grpc.parser import GRPCParser
from chilo_api.cli.grpc.scanner import GRPCScanner


def __run_server(server):
    gprc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    gprc_server.add_insecure_port(f'[::]:{server.port}')  # 50051
    gprc_server.start()
    gprc_server.wait_for_termination()


def __generate_middleware_objects(server, endpoints):
    parser = GRPCParser()
    for endpoint in endpoints:
        result = parser.parse_proto_file(server, endpoint)
        for statement in result.statements:
            class_name = type(statement).__name__
            if class_name == 'Package':
                endpoint.package_identifier = statement.identifer[0]
            if class_name == 'Service':
                endpoint.service_name = statement.name
                endpoint.response_func_name = statement.body[0].response_message_type
                endpoint.request_stream = statement.body[0].request_stream
                endpoint.response_stream = statement.body[0].response_stream
        print(endpoint)
            # use data from statement to find identifer, name, request_message_type, response_message_type, and string match function
            # https://stackoverflow.com/questions/15247075/how-can-i-dynamically-create-derived-classes-from-a-base-class


def __generate_grpc_code(server):
    scanner = GRPCScanner()
    importer = GRPCImporter()
    commander = GRPCCommander()

    handlers = scanner.get_gprc_handers(server.handlers)
    modules = importer.get_imported_modules(handlers)
    endpoints = GRPCEndpoint.get_endpoints_from_modules(modules)
    commander.generate_grpc_code(endpoints, server)
    return endpoints


def run_grpc_simple(server):
    endpoints = __generate_grpc_code(server)
    __generate_middleware_objects(server, endpoints)
    # __run_server(server)
