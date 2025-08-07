from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request as WSGIRequest, Response as WSGIResponse

from chilo_api.core.rest.request import RestRequest as Request
from chilo_api.core.rest.response import Response


class EnvironmentBuilder:

    @property
    def mock_request_class(self):
        return WSGIRequest

    @property
    def mock_response_class(self):
        return WSGIResponse

    def mock_start_response(self, status, headers, **_):
        return {
            'status': status,
            'headers': headers
        }

    def get_environ(self, **kwargs):
        return EnvironBuilder(**kwargs).get_environ()

    def get_request(self, timeout=None, **kwargs):
        return Request(wsgi=WSGIRequest(environ=EnvironBuilder(**kwargs).get_environ()), timeout=timeout)

    def get_response(self):
        return Response(wsgi=WSGIResponse, environ=EnvironBuilder().get_environ(), server_response=self.mock_start_response)
