from concurrent import futures
import grpc

from chilo_api.cli.grpc.commander import GRPCCommander
from chilo_api.cli.grpc.endpoint import GRPCEndpoint
from chilo_api.cli.grpc.importer import GRPCImporter
from chilo_api.cli.grpc.scanner import GRPCScanner


def run_server(server):
    gprc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    gprc_server.add_insecure_port(f'[::]:{server.port}')  # 50051
    gprc_server.start()
    gprc_server.wait_for_termination()


def generate_grpc_code(server):
    scanner = GRPCScanner()
    importer = GRPCImporter()
    commander = GRPCCommander()

    handlers = scanner.get_gprc_handers(server.handlers)
    modules = importer.get_imported_modules(handlers)
    endpoints = GRPCEndpoint.get_endpoints_from_modules(modules)
    commander.generate_grpc_code(endpoints, server)
    for endpoint in endpoints:
        print(endpoint)


def run_grpc_simple(server):
    generate_grpc_code(server)
    # run_server(server)
