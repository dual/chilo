from chilo_api.cli.grpc.parser.parsey_proto import proto


class GRPCParser:

    def parse_proto_file(self, server, endpoint):
        proto_file_path = f'{server.protobufs}/{endpoint.protobuf}'
        with open(proto_file_path, 'r') as file:
            proto_string = file.read()
        return proto.parse(proto_string)
