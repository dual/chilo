import base64
import gzip
from io import BytesIO

from chilo.core.json_helper import JsonHelper


class Response:

    def __init__(self, **kwargs):
        self.__code = 200
        self.__is_json = True
        self.__cors = kwargs.get('cors', True)
        self.__base64_encoded = False
        self.__compress = False
        self.__mimetype = 'application/json'
        self.__server_response = kwargs['server_response']
        self.__wsgi = kwargs['wsgi']
        self.__environ = kwargs['environ']
        self.__headers = {}
        self.__body = {}

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, header):
        key, value = header
        self.__headers[key] = value

    @property
    def mimetype(self):
        return self.__mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        self.__mimetype = mimetype

    @property
    def cors(self):
        return self.__cors

    @cors.setter
    def cors(self, access):
        self.__cors = access

    @property
    def open_cors(self):
        return self.__cors

    @open_cors.setter
    def open_cors(self, access):
        self.__cors = access

    @property
    def base64_encoded(self):
        return self.__base64_encoded

    @property
    def compress(self):
        return self.__compress

    @compress.setter
    def compress(self, value):
        self.__compress = value

    @property
    def code(self):
        if isinstance(self.__body, dict) and self.__code == 200 and not self.__body:
            return 204
        if isinstance(self.__body, dict) and self.__code == 200 and self.has_errors:
            return 400
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def is_json(self):
        return self.__is_json

    @is_json.setter
    def is_json(self, is_json):
        self.__is_json = is_json

    @property
    def has_errors(self):
        return 'errors' in self.__body

    @property
    def body(self):
        if self.compress:
            return self.__compress_body(JsonHelper.encode(self.__body, raise_error=True))
        if isinstance(self.__body, (dict, list, tuple)):
            return JsonHelper.encode(self.__body, raise_error=True)
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def raw(self):
        return self.__body

    @property
    def server(self):
        response = self.__wsgi(self.body, mimetype=self.mimetype)
        return response(self.__environ, self.__server_response)

    def set_error(self, key_path, message):
        error = {'key_path': key_path, 'message': message}
        if isinstance(self.__body, dict) and 'errors' in self.__body:
            self.__body['errors'].append(error)
        else:
            self.__body = {'errors': [error]}

    def __compress_body(self, body):
        self.headers = ('Content-Encoding', 'gzip')
        self.__base64_encoded = True
        bytes_io = BytesIO()
        with gzip.GzipFile(fileobj=bytes_io, mode='w') as file:
            file.write(body.encode('utf-8'))
        return base64.b64encode(bytes_io.getvalue()).decode('ascii')
