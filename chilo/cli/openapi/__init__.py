import pprint
from icecream import ic

from chilo.cli.openapi.handler.importer import HandlerImporter
from chilo.cli.openapi.handler.scanner import HandlerScanner
from chilo.cli.openapi.input.arguments import InputArguments
from chilo.cli.openapi.input.validator import InputValidator
from chilo.cli.openapi.generator import OpenAPIGenerator
from chilo.cli.openapi.file_writer import OpenAPIFileWriter


def generate_openapi(args):
    print('STARTED')
    print('generating openapi docs...')
    print('validating arguments received...')
    inputs = InputArguments(args)
    validator = InputValidator()
    scanner = HandlerScanner(inputs.handlers)
    importer = HandlerImporter()
    generator = OpenAPIGenerator(inputs.output)
    writer = OpenAPIFileWriter()

    validator.validate_arguments(inputs)
    print('arguments validated...')
    file_paths = scanner.get_handler_file_paths()
    print(f'scanning handlers: {inputs.handlers}...')
    modules = importer.get_modules_from_file_paths(file_paths, scanner.handlers_base, inputs.base)
    print('importing handler endpoint modules...')

    for module in modules:
        generator.add_path_and_method(module)

    if inputs.delete:
        print('deleting paths and methods not found in code base')
        generator.delete_unused_paths()

    print(f'writing openapi doc to requested directory: {inputs.output}')
    writer.write_openapi(generator.doc, inputs.output, inputs.formats)
    print('COMPLETED')
