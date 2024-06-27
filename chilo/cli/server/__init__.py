import importlib.util

from chilo import Chilo
import os


def run_server(args):
    cwd = os.getcwd()
    file_path = f'{cwd}/{args.api}'
    import_path = file_path.replace('/', '.')
    spec = importlib.util.spec_from_file_location(import_path, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    matches = [v for v in module.__dict__.values() if isinstance(v, Chilo)]
    api = matches[0]
    print(api.test)


# if __name__ == '__main__':
    #     run_simple('127.0.0.1', 5000, api_server.route)

    # def find_best_app(module: ModuleType) -> Flask:
    #     """Given a module instance this tries to find the best possible
    #     application in the module or raises an exception.
    #     """
    #     from . import Flask

    #     # Search for the most common names first.
    #     for attr_name in ("app", "application"):
    #         app = getattr(module, attr_name, None)

    #         if isinstance(app, Flask):
    #             return app

    #     # Otherwise find the only object that is a Flask instance.
    #     matches = [v for v in module.__dict__.values() if isinstance(v, Flask)]

    # run_simple(
    #     host,
    #     port,
    #     app,
    #     use_reloader=reload,
    #     use_debugger=debugger,
    #     threaded=with_threads,
    #     ssl_context=cert,
    #     extra_files=extra_files,
    #     exclude_patterns=exclude_patterns,
    # )
