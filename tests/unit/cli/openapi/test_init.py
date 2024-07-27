from unittest import mock, TestCase

from chilo_api.cli.openapi import generate_openapi
from chilo_api.cli import CliManager


def mock_open(*args, **kwargs):
    pass


class GenerateOpenApiTest(TestCase):

    @mock.patch('sys.argv', [
        'CliManager',
        'generate-openapi',
        '--api=api',
        '--output=tests',
        '--format=json,yml',
        '--delete'
    ])
    @mock.patch('chilo_api.cli.openapi.OpenAPIFileWriter.write_openapi', mock_open)
    def test_generate_openapi(self):
        manager = CliManager()
        generate_openapi(manager.args)
        self.assertTrue(True)  # should error and fail test if broken

    @mock.patch('sys.argv', [
        'CliManager',
        'generate-openapi',
        '--api=api',
        '--output=tests/mocks/openapi/discoverable/removed',
        '--format=json,yml',
        '--delete'
    ])
    @mock.patch('chilo_api.cli.openapi.OpenAPIFileWriter.write_openapi', mock_open)
    def test_generate_openapi_with_removed_paths_and_methods(self):
        manager = CliManager()
        generate_openapi(manager.args)
        self.assertTrue(True)  # should error and fail test if broken

    @mock.patch('sys.argv', [
        'CliManager',
        'generate-openapi',
        '--api=api',
        '--output=tests/mocks/openapi/discoverable/existing',
        '--format=json,yml',
        '--delete'
    ])
    @mock.patch('chilo_api.cli.openapi.OpenAPIFileWriter.write_openapi', mock_open)
    def test_generate_openapi_with_existing_json(self):
        manager = CliManager()
        generate_openapi(manager.args)
        self.assertTrue(True)  # should error and fail test if broken
