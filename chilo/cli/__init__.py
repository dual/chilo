import argparse

from chilo.cli.openapi import generate_openapi
from chilo.cli.server import run_server


class CliManager:

    def __init__(self):
        self.__args = self.__get_command_line_args()

    def run(self):
        if self.__args.action == 'generate-openapi':
            generate_openapi(self.__args)
        elif self.__args.action == 'serve':
            run_server(self.__args)

    def __get_command_line_args(self):
        parser = argparse.ArgumentParser(
            prog='Acai AWS: OpenApi Generator',
            description='Will generate an openapi yml file based on your api project'
        )
        parser.add_argument(
            'action',
            help='the action to take',
            choices=['generate-openapi', 'serve']
        )
        parser.add_argument(
            '-a',
            '--api',
            help='api file to run',
            required=False
        )
        parser.add_argument(
            '-b',
            '--base',
            help='base path of the api url; (optional) default=/',
            default='/',
            required=False
        )
        parser.add_argument(
            '-l',
            '--handlers',
            help='directory or pattern location of your handlers',
            required=False
        )
        parser.add_argument(
            '-o',
            '--output',
            help='(optional) directory location to save openapi file; defaults handlers directory location',
            required=False
        )
        parser.add_argument(
            '-f',
            '--format',
            help='(optional) comma deliminted format options (yml, json)',
            choices=['yml', 'json', 'yml,json', 'json,yml'],
            required=False
        )
        parser.add_argument(
            '-d',
            '--delete',
            help='(optional) will delete routes and methods not found in code base',
            action='store_true',
            required=False
        )
        parser.add_argument(
            '-s',
            '--host',
            help='(optional) host ip/domain for server; default: 127.0.0.1',
            default='127.0.0.1',
            required=False
        )
        parser.add_argument(
            '-p',
            '--port',
            help='(optional) port to run server on; default 3000',
            default=3000,
            required=False
        )
        parser.add_argument(
            '-r',
            '--reload',
            help='(optional) will reload app on file change; default: True',
            action='store_true',
            required=False
        )
        parser.add_argument(
            '-u',
            '--debugger',
            help='(optional) will run server in debugger mode; default: False',
            action='store_false',
            required=False
        )
        return parser.parse_args()
