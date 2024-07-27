import os
import unittest

from chilo_api.cli.openapi.handler.scanner import HandlerScanner


class HandlerScannerTest(unittest.TestCase):
    handler_path = 'tests/mocks/handlers/valid/**/*.py'

    def setUp(self):
        self.scanner = HandlerScanner(self.handler_path)

    def test_file_separator(self):
        self.assertEqual(self.scanner.file_separator, os.sep)

    def test_handlers(self):
        self.assertEqual(self.scanner.handlers, self.handler_path)

    def test_handlers_base(self):
        self.assertEqual(self.scanner.handlers_base, 'tests/mocks/handlers/valid')

    def test_clean_path(self):
        dirty_path = '/dirty/path/'
        result = self.scanner.clean_path(dirty_path)
        self.assertEqual(result, 'dirty/path')

    def test_get_handler_file_paths(self):
        paths = self.scanner.get_handler_file_paths()
        self.assertEqual(len(paths), 21)

    def test_get_handler_file_no_directory(self):
        scanner = HandlerScanner('tests/mocks/handlers/valid')
        paths = scanner.get_handler_file_paths()
        self.assertEqual(len(paths), 21)
