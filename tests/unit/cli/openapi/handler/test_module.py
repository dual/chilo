import importlib.util
import unittest

from chilo_api.cli.openapi.handler.module import HandlerModule


class HandlerModuleTest(unittest.TestCase):

    def __setup_module(self, **kwargs):
        file_path = kwargs.get('file_path', 'tests/mocks/handlers/valid/basic.py')
        import_path = kwargs.get('import_path', 'tests.mocks.handlers.basic')
        method = kwargs.get('method', 'post')
        spec = importlib.util.spec_from_file_location(import_path, file_path)
        handler_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(handler_module)
        return HandlerModule('tests/mocks', file_path, handler_module, method, 'chilo/example')

    def setUp(self):
        self.module = self.__setup_module()

    def test_file_path(self):
        self.assertEqual(self.module.file_path, 'tests/mocks/handlers/valid/basic.py')

    def test_module(self):
        self.assertEqual(len(dir(self.module.module)), 15)

    def test_method(self):
        self.assertEqual(self.module.method, 'post')

    def test_operation_id(self):
        self.assertEqual(self.module.operation_id, 'PostChiloExampleHandlersValidBasicChiloGenerated')

    def test_route_path(self):
        self.assertEqual(self.module.route_path, '/chilo/example/handlers/valid/basic')

    def test_deprecated(self):
        self.assertEqual(self.module.deprecated, False)

    def test_summary(self):
        self.assertEqual(self.module.summary, None)

    def test_tags(self):
        self.assertListEqual(['chilo-example'], self.module.tags)

    def test_requires_auth(self):
        self.assertEqual(self.module.requires_auth,  True)

    def test_required_headers(self):
        self.assertListEqual([], self.module.required_headers)

    def test_available_headers(self):
        self.assertListEqual([], self.module.available_headers)

    def test_required_query(self):
        self.assertListEqual([], self.module.required_query)

    def test_available_query(self):
        self.assertListEqual([], self.module.available_query)

    def test_required_path_params(self):
        self.assertListEqual([], self.module.required_path_params)

    def test_required_path_params(self):
        self.assertEqual(self.module.request_body_schema_name, 'post-chilo-example-handlers-valid-basic-request-body')

    def test_response_body_schema_name(self):
        self.assertEqual(self.module.response_body_schema_name, 'post-chilo-example-handlers-valid-basic-response-body')

    def test_request_body_schema(self):
        expected = {
            'title': 'UserRequest',
            'type': 'object',
            'required': ['id', 'email', 'active', 'favorites', 'notification_config'],
            'properties': {
                'id': {
                    'exclusiveMinimum': 0,
                    'title': 'Id',
                    'type': 'integer'
                },
                'email': {
                    'title': 'Email',
                    'type': 'string'
                },
                'active': {
                    'title': 'Active',
                    'type': 'boolean'
                },
                'favorites': {
                    'items': {'type': 'string'},
                    'title': 'Favorites',
                    'type': 'array'
                },
                'notification_config': {
                    'additionalProperties': {'type': 'boolean'},
                    'title': 'Notification Config',
                    'type': 'object'
                }
            }
        }
        self.assertDictEqual(expected, self.module.request_body_schema)

    def test_request_body_schema(self):
        assert self.module.response_body_schema is None

    def test_dynamic_route_path(self):
        module = self.__setup_module(
            method='get',
            file_path='tests/mocks/handlers/valid/user/_user_id/item/_item_id.py',
            import_path='tests.mocks.handlers.user._user_id.item._item_id'
        )
        self.assertEqual(module.route_path, '/user/{user_id}/item/{item_id}')
