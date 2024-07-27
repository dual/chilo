import unittest
from unittest.mock import patch

from chilo_api.cli.openapi.input.arguments import InputArguments
from chilo_api.cli.server.importer import ServerImporter
from chilo_api.cli import CliManager


class InputArgumentsTest(unittest.TestCase):

    @patch('sys.argv', [
        'CliManager',
        'generate-openapi',
        '--api=api',
        '--output=tests/outputs/arguments',
        '--format=json,yml',
        '--delete'
    ])
    def test_full_class(self):
        manager = CliManager()
        importer = ServerImporter(manager.args.api)
        api = importer.get_api_module()
        input_args = InputArguments(api, manager.args)
        self.assertEqual('/', input_args.base)
        self.assertEqual('tests/mocks/handlers/valid', input_args.handlers)
        self.assertEqual('tests/outputs/arguments', input_args.output)
        self.assertListEqual(['json', 'yml'], input_args.formats)
        self.assertTrue(input_args.delete)
