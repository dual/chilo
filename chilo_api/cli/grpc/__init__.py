import glob
import importlib
import os
import subprocess


def get_glob_pattern(handlers):
    if '*' in handlers and '.py' in handlers:
        return handlers
    return handlers + os.sep + '**' + os.sep + '*.py'


def get_protobuf(file_list):
    protobufs = set()
    for file_path in file_list:
        import_path = file_path.replace('/', '.')
        spec = importlib.util.spec_from_file_location(import_path, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        rpcs = [v for v in dir(module) if v and v.startswith('rpc_')]
        for rpc in rpcs:
            func = getattr(module, rpc)
            reqs = getattr(func, 'requirements', {})
            if reqs.get('protobuf'):
                protobufs.add(reqs['protobuf'])
    return protobufs


def run_command(protobufs, server):
    for protobuf in protobufs:
        protobuf_path = f'{server.protobufs}/{protobuf}'
        print()
        subprocess.run(['python', '-m', 'grpc_tools.protoc', '-I.', '--python_out=.', '--pyi_out=.', '--grpc_python_out=.', protobuf_path])


def import_rpc_funcs(server):
    glob_pattern = get_glob_pattern(server.handlers)
    file_list = glob.glob(glob_pattern, recursive=True)
    protobufs = get_protobuf(file_list)
    run_command(protobufs, server)
    return protobufs
