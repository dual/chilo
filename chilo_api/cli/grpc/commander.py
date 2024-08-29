import subprocess


class GRPCCommander:

    def generate_grpc_code(self, endpoints, server):
        for endpoint in endpoints:
            generated = f'{server.protobufs}/generated'
            file = f'{server.protobufs}/{endpoint.protobuf}'
            command = ['python', '-m', 'grpc_tools.protoc']
            args = f'--proto_path={server.protobufs} --python_out={generated} --pyi_out={generated} --grpc_python_out={generated} {file}'
            command.extend(args.split())
            subprocess.run(command)