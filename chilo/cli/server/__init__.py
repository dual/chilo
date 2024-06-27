import os
import importlib.util
from werkzeug.serving import run_simple

from chilo import Chilo


def run_server(args):
    cwd = os.getcwd()
    file_path = f'{cwd}/{args.api}'
    import_path = file_path.replace('/', '.')
    spec = importlib.util.spec_from_file_location(import_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    matches = [v for v in module.__dict__.values() if isinstance(v, Chilo)]
    api = matches[0]
    run_simple(args.host, args.port, api.route, use_reloader=args.reload, use_debugger=args.debugger)


# @TODO
# Create class for inputs for sever (with defaults)
# create a class for importing the module
# Create class for validation of those inputs
# Add props to chilo init file for server config-based properties
# Add exceptions where appropriate
