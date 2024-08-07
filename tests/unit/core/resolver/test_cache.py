import unittest

from chilo_api.core.endpoint import Endpoint
from chilo_api.core.resolver.cache import ResolverCache
from chilo_api.core.resolver.importer import ResolverImporter


class ResolverCacheTest(unittest.TestCase):
    handler_path = 'tests/mocks/handlers/unit_tests/valid'
    file_path = f'{handler_path}/basic.py'
    import_path = 'tests.mocks.handlers.basic'

    def setUp(self):
        self.importer = ResolverImporter(handlers=self.handler_path)

    def test_cache_settings(self):
        cacher = ResolverCache()
        self.assertTrue(cacher.CACHE_ALL == 'all')
        self.assertTrue(cacher.CACHE_STATIC == 'static-only')
        self.assertTrue(cacher.CACHE_DYNAMIC == 'dynamic-only')

    def test_cache_put(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        endpoint = Endpoint(endpoint_module, 'post')
        cacher = ResolverCache()
        cacher.put('post::/unit-test/v1/cacher/basic', endpoint, False, {})
        self.assertTrue(True)

    def test_cache_put_and_get(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache()
        cacher.put('get::/unit-test/v1/cacher/basic', endpoint, False, {})
        cached = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(cached['endpoint'].has_requirements)

    def test_cache_get_miss(self):
        cacher = ResolverCache()
        cached = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(cached.get('endpoint') is None)

    def test_cache_lru_sequence_size_reaches_capacity_and_result_in_miss(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        post_endpoint = Endpoint(endpoint_module, 'post')
        delete_endpoint = Endpoint(endpoint_module, 'delete')
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache(cache_size=1)
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, False, {})
        get_cache_result = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(get_cache_result['endpoint'].has_requirements)
        cacher.put('delete::/unit-test/v1/cacher/basic', delete_endpoint, False, {})
        cacher.get('delete::/unit-test/v1/cacher/basic')
        cacher.put('post::/unit-test/v1/cacher/basic', post_endpoint, False, {})
        cacher.get('post::/unit-test/v1/cacher/basic')
        miss_cache_result = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(miss_cache_result.get('endpoint') is None)

    def test_cache_size_none_always_miss(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache(cache_size=None)
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, False, {})
        get_cache_result = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(get_cache_result.get('endpoint') is None)

    def test_cache_static_only(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache(cache_mode='static-only')
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, False, {})
        get_cache_result = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(get_cache_result['endpoint'].has_requirements)
        patch_endpoint = Endpoint(endpoint_module, 'patch')
        cacher.put('patch::/unit-test/v1/cacher/basic', patch_endpoint, True, {'1': 1})
        patch_cache_result = cacher.get('patch::/unit-test/v1/cacher/basic')
        self.assertTrue(patch_cache_result.get('endpoint') is None)

    def test_cache_dynamic_only(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache(cache_mode='dynamic-only')
        delete_endpoint = Endpoint(endpoint_module, 'delete')
        cacher.put('delete::/unit-test/v1/cacher/basic', delete_endpoint, True, {'1': 1})
        delete_cache_result = cacher.get('delete::/unit-test/v1/cacher/basic')
        self.assertTrue(delete_cache_result['endpoint'].has_requirements)
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, False, {})
        get_cache_result = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(get_cache_result.get('endpoint') is None)

    def test_cache_remembers_is_dynamic_route(self):
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache()
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, True, {'1': 1})
        cached = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertTrue(cached['is_dynamic_route'])

    def test_cache_remembers_dynamic_parts(self):
        dynamic_parts = {'1': 1}
        endpoint_module = self.importer.import_module_from_file(self.file_path, self.import_path)
        get_endpoint = Endpoint(endpoint_module, 'get')
        cacher = ResolverCache()
        cacher.put('get::/unit-test/v1/cacher/basic', get_endpoint, True, dynamic_parts)
        cached = cacher.get('get::/unit-test/v1/cacher/basic')
        self.assertDictEqual(cached['dynamic_parts'], dynamic_parts)
