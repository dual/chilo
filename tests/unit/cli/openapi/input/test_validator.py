import unittest

from chilo_api.cli.openapi.input.validator import InputValidator


class MockInputArguments:

    def __init__(self):
        self.base = 'chilo/example'
        self.handlers = 'tests/mocks/openapi/**/*.py'
        self.output = 'tests/mocks'
        self.format = 'json,yml'


class InputValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = InputValidator()

    def test_validate_arguments_all_pass(self):
        inputs = MockInputArguments()
        self.validator.validate_arguments(inputs)

    def test_validate_arguments_directory_fails(self):
        try:
            inputs = MockInputArguments()
            inputs.output = 'tests/fail'
            self.validator.validate_arguments(inputs)
            self.assertTrue(False)
        except Exception as error:
            self.assertTrue('is not a valid directory path' in repr(error))
