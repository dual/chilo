import base64

import xmltodict

from chilo.core.json_helper import JsonHelper
from chilo.core import logger


class Request:

    def __init__(self, **kwargs):
        self.__wsgi = kwargs['wsgi']
        self.__timeout = kwargs['timeout']
        self.__data = self.__wsgi.get_data(as_text=True, cache=False)
        self.__route = self.__wsgi.path
        self.__path_params = {}
        self.__context = {}
        self.__parsers = {
            'application/json': 'json',
            'application/graphql': 'graphql',
            'application/x-www-form-urlencoded': 'form',
            'multipart/form-data': 'raw',
            'application/xml': 'xml',
            'text/xml': 'xml',
            'raw': 'raw'
        }

    @property
    def cookies(self):
        return self.__wsgi.cookies

    @property
    def protocol(self):
        return self.__wsgi.scheme

    @property
    def content_type(self):
        return self.__wsgi.content_type

    @property
    def mimetype(self):
        return self.__wsgi.mimetype

    @property
    def host_url(self):
        return self.__wsgi.host_url

    @property
    def domain(self):
        pass

    @property
    def method(self):
        return self.__wsgi.method.lower()

    @property
    def path(self):
        return self.__wsgi.path

    @property
    def route(self):
        if self.__route and self.__route[0] != '/':
            return f'/{self.__route}'
        return self.__route

    @route.setter
    def route(self, route):
        self.__route = route

    @property
    def headers(self):
        return dict(self.__wsgi.headers)

    @property
    def body(self):
        try:
            parser = self.__parsers.get(self.mimetype, 'raw')
            return getattr(self, parser)
        except Exception as error:
            logger.log(level='ERROR', log=error)
            return self.__data

    @property
    def json(self):
        return JsonHelper.decode(self.__data)

    @property
    def form(self):
        return self.__wsgi.form

    @property
    def xml(self):
        return xmltodict.parse(self.__data)

    @property
    def files(self):
        return self.__wsgi.files

    @property
    def graphql(self):
        try:
            graphql_body = base64.b64decode(self.__data).decode('utf-8')
        except Exception as error:
            logger.log(level='ERROR', log=error)
            graphql_body = self.__data
        return JsonHelper.decode(graphql_body)

    @property
    def raw(self):
        return self.__wsgi.get_data()

    @property
    def query_params(self):
        return self.__wsgi.args

    @property
    def path_params(self):
        return self.__path_params

    @path_params.setter
    def path_params(self, path_params):
        key, value = path_params
        self.__path_params[key] = value

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context):
        self.__context = context

    @property
    def timeout(self):
        return self.__timeout

    def clear_path_params(self):
        self.__path_params = {}

    def __str__(self):
        return JsonHelper.encode({
            'method': self.method,
            'resource': self.resource,
            'headers': self.headers,
            'query': self.query_params,
            'path': self.path_params,
            'body': self.body,
            'context': self.context
        })
