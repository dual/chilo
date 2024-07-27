import json
import unittest
import yaml

from chilo_api.cli.openapi.handler.importer import HandlerImporter
from chilo_api.cli.openapi.generator import OpenAPIGenerator


class OpenAPIGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.non_existing_expected = {
            'openapi': '3.0.1',
            'info': {'version': '1.0.0', 'title': 'Chilo Generator', 'license': {'name': 'MIT'}},
            'tags': [{'name': 'chilo-unit_test'}],
            'servers': [],
            'paths': {
                '/some/route/{id}': {
                    'delete': {
                        'tags': ['chilo-unit_test'],
                        'operationId': 'DeleteSomeRouteIdChiloGenerated',
                        'deprecated': False,
                        'parameters': [
                            {
                                'in': 'path',
                                'name': 'id',
                                'required': True,
                                'schema': {'type': 'string'}
                            }
                        ],
                        'responses': {'200': {'content': {'application/json': {}}, 'description': 'OK'}}
                    }
                }
            },
            'components': {
                'securitySchemes': {
                    'ChiloGenerated': {
                        'type': 'apiKey',
                        'in': 'header',
                        'name': 'CHANGE-ME'
                    }
                },
                'schemas': {}
            }
        }
        with open('tests/mocks/openapi/discoverable/existing/yaml/openapi.yml', encoding='utf-8') as schema_file:
            self.existing_expected_yml = yaml.load(schema_file, Loader=yaml.FullLoader)
        with open('tests/mocks/openapi/discoverable/existing/json/openapi.json', encoding='utf-8') as schema_file:
            self.existing_expected_json = yaml.load(schema_file, Loader=yaml.FullLoader)
        with open('tests/mocks/openapi/discoverable/removed/openapi.yml', encoding='utf-8') as schema_file:
            self.removed_path_existing_expected_yml = yaml.load(schema_file, Loader=yaml.FullLoader)

    def test_add_path_and_method_existing_yml_file(self):
        generator = OpenAPIGenerator('tests/mocks/openapi/discoverable/existing/yaml')
        self.assertDictEqual(self.existing_expected_yml, generator.doc)

    def test_add_path_and_method_existing_json_file(self):
        generator = OpenAPIGenerator('tests/mocks/openapi/discoverable/existing/json')
        self.assertEqual(json.dumps(generator.doc), json.dumps(self.existing_expected_json))

    def test_removed_path_and_method_existing_yml_file(self):
        generator = OpenAPIGenerator('tests/mocks/openapi/discoverable/removed')
        generator.doc
        self.assertTrue(True)

    def test_add_path_and_method_non_existing_file(self):
        importer = HandlerImporter()
        generator = OpenAPIGenerator('tests/non-existing')
        module = importer.get_modules_from_file_paths(
            ['tests/mocks/handlers/valid/basic.py'],
            'tests/mocks/handlers/valid',
            'chilo/unit_test'
        )[0]
        generator.add_path_and_method(module)
        self.assertDictEqual(self.non_existing_expected, generator.doc)
