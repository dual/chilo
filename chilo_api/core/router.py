import datetime

from werkzeug.wrappers import Request as WSGIRequest, Response as WSGIResponse

from chilo_api.core.logger.common import CommonLogger
from chilo_api.core.exception import ApiException, ApiTimeOutException
from chilo_api.core.validator.config import ConfigValidator
from chilo_api.core.json_helper import JsonHelper
from chilo_api.core.request import Request
from chilo_api.core.resolver import Resolver
from chilo_api.core.response import Response
from chilo_api.core.validator import Validator


class Router:

    def __init__(self, **kwargs):
        ConfigValidator.validate(**kwargs)
        self.__handlers = kwargs['handlers']
        self.__base_path = kwargs['base_path']
        self.__host = kwargs.get('host', '127.0.0.1')
        self.__port = kwargs.get('port', 3000)
        self.__reload = kwargs.get('reload', False)
        self.__verbose = kwargs.get('verbose', False)
        self.__before_all = kwargs.get('before_all')
        self.__after_all = kwargs.get('after_all')
        self.__when_auth_required = kwargs.get('when_auth_required')
        self.__on_error = kwargs.get('on_error')
        self.__on_timeout = kwargs.get('on_timeout')
        self.__cors = kwargs.get('cors', True)
        self.__timeout = kwargs.get('timeout', None)
        self.__output_error = kwargs.get('output_error', False)
        self.__openapi_validate_request = kwargs.get('openapi_validate_request', False)
        self.__openapi_validate_response = kwargs.get('openapi_validate_response', False)
        self.__resolver = Resolver(**kwargs)
        self.__validator = Validator(**kwargs)
        self.__logger = CommonLogger(**kwargs)
        self.__resolver.auto_load()
        self.__validator.auto_load()

    @property
    def handlers(self):
        return self.__handlers

    @property
    def base_path(self):
        return self.__base_path

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def reload(self):
        return self.__reload

    @property
    def verbose(self):
        return self.__verbose

    def route(self, environ, server_response):
        request = Request(wsgi=WSGIRequest(environ), timeout=self.__timeout)
        response = Response(cors=self.__cors, wsgi=WSGIResponse, environ=environ, server_response=server_response)
        try:
            self.__run_route_procedure(request, response)
        except ApiTimeOutException as timeout_error:
            kwargs = {'code': timeout_error.code, 'key_path': timeout_error.key_path, 'message': timeout_error.message, 'error': timeout_error}
            self.__handle_error(request, response, self.__on_timeout, **kwargs)
        except ApiException as api_error:
            kwargs = {'code': api_error.code, 'key_path': api_error.key_path, 'message': api_error.message, 'error': api_error}
            self.__handle_error(request, response, self.__on_error, **kwargs)
        except Exception as error:
            output = str(error) if self.__output_error else 'internal service error'
            kwargs = {'code': 500, 'key_path': 'unknown', 'message': output, 'error': error}
            self.__handle_error(request, response, **kwargs)
        self.__log_verbose(request, response)
        self.__resolver.reset()
        return response.server

    def __run_route_procedure(self, request, response):
        endpoint = self.__resolver.get_endpoint(request)
        self.__run_before_all(request, response, endpoint)
        self.__run_when_auth_required(request, response, endpoint)
        self.__run_request_validation(request, response, endpoint)
        if not response.has_errors:
            endpoint.run(request, response)
        self.__run_response_validation(request, response, endpoint)
        self.__run_after_all(request, response, endpoint)
        return response

    def __run_before_all(self, request, response, endpoint):
        if not response.has_errors and self.__before_all and callable(self.__before_all):
            self.__before_all(request, response, endpoint.requirements)

    def __run_when_auth_required(self, request, response, endpoint):
        if not response.has_errors and self.__when_auth_required and callable(self.__when_auth_required):
            if (self.__openapi_validate_request and self.__validator.request_has_security(request)) or endpoint.requires_auth:
                self.__when_auth_required(request, response, endpoint.requirements)

    def __run_request_validation(self, request, response, endpoint):
        if not response.has_errors and self.__openapi_validate_request:
            self.__validator.validate_request_with_openapi(request, response)
        elif not response.has_errors and endpoint.has_requirements:
            self.__validator.validate_request(request, response, endpoint.requirements)

    def __run_response_validation(self, request, response, endpoint):
        if not response.has_errors and self.__openapi_validate_response:
            self.__validator.validate_response_with_openapi(request, response)
        elif not response.has_errors and endpoint.has_required_response:
            self.__validator.validate_response(response, endpoint.requirements)

    def __run_after_all(self, request, response, endpoint):
        if not response.has_errors and self.__after_all and callable(self.__after_all):
            self.__after_all(request, response, endpoint.requirements)

    def __handle_error(self, request, response, error_func=None, **kwargs):
        try:
            response.code = kwargs['code']
            response.set_error(key_path=kwargs['key_path'], message=kwargs['message'])
            if error_func and callable(error_func):
                error_func(request, response, kwargs.get('error'))
            else:
                self.__logger.log(level='ERROR', log={'request': request, 'response': response, 'error': kwargs})
        except Exception as exception:
            self.__logger.log(level='ERROR', log=exception)

    def __log_verbose(self, request, response):
        if self.__verbose:
            self.__logger.log(
                level='DEBUG',
                log={
                    '_timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'request': JsonHelper.decode(str(request)),
                    'response': JsonHelper.decode(str(response))
                }
            )
