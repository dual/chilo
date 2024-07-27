import unittest

from chilo_api.cli.openapi.handler.importer import HandlerImporter


class HandlerImporterTest(unittest.TestCase):

    def test_get_modules_from_file_paths(self):
        importer = HandlerImporter()
        file_paths = ['tests/mocks/handlers/valid/basic.py']
        handlers_base = 'tests/mocks/handlers/valid'
        base_path = 'chilo/example'
        modules = importer.get_modules_from_file_paths(file_paths, handlers_base, base_path)
        assert len(modules) == 5
