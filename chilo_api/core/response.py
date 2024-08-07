import base64
import gzip
from io import BytesIO

from chilo_api.core.json_helper import JsonHelper


class Response:
    '''
    A class to represent a api response

    Attributes
    ----------
    headers: dict
        The headers of the response (case sensitive)
    mimetype: str
        The mimetype (content type without charset etc.)
    cors: str, boolean
        determines if cors is enabled; can set `True` to open cors, or set a comma delimented string for only certain domains
    compress: boolean
        determines if response will be compressed (defaults is `False`)
    code: int (1xx - 5xx)
        status code to be returned to requester
    has_errors: bool
        determines if body contains error object
    body: str
        the return body of the response in json string
    raw: dict, list tuple
        the return body of the request in its original format
    server: any
        special return format for use by the server worker
    
    Methods
    ----------
    set_error(key_path, message):
        composes error using consistent format
    '''

    def __init__(self, **kwargs):
        self.__code = 200
        self.__cors = kwargs.get('cors')
        self.__compress = False
        self.__mimetype = 'application/json'
        self.__server_response = kwargs['server_response']
        self.__wsgi = kwargs['wsgi']
        self.__environ = kwargs['environ']
        self.__headers = {}
        self.__body = None

    @property
    def headers(self):
        if isinstance(self.cors, bool) and self.cors:
            self.headers = ('Access-Control-Allow-Origin', '*')
        elif isinstance(self.cors, str) and 'Access-Control-Allow-Origin' not in self.__headers:
            self.headers = ('Access-Control-Allow-Origin', self.cors)
        return self.__headers

    @headers.setter
    def headers(self, header):
        key, value = header
        self.__headers[key] = value

    @property
    def mimetype(self):
        if 'Content-Type' in self.headers:
            self.__mimetype = self.headers['Content-Type'].split(';')[0]
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
    def compress(self):
        return self.__compress

    @compress.setter
    def compress(self, value):
        self.__compress = value

    @property
    def code(self):
        if self.__body is None and self.__code == 200:
            self.__code = 204
        elif isinstance(self.__body, dict) and self.__code == 200 and self.has_errors:
            self.__code = 400
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def has_errors(self):
        return 'errors' in self.__body if isinstance(self.__body, dict) else False

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
        response = self.__wsgi(self.body, headers=self.headers, mimetype=self.mimetype, status=self.code)
        return response(self.__environ, self.__server_response)

    def set_error(self, key_path, message):
        error = {'key_path': key_path, 'message': message}
        if isinstance(self.__body, dict) and 'errors' in self.__body:
            self.__body['errors'].append(error)
        else:
            self.__body = {'errors': [error]}

    def __compress_body(self, body):
        self.headers = ('Content-Encoding', 'gzip')
        bytes_io = BytesIO()
        with gzip.GzipFile(fileobj=bytes_io, mode='w') as file:
            file.write(body.encode('utf-8'))
        return base64.b64encode(bytes_io.getvalue()).decode('ascii')

    def __str__(self):
        return str({
            'headers': self.headers,
            'mimetype': self.mimetype,
            'cors': self.cors,
            'compress': self.compress,
            'code': self.code,
            'body': self.raw
        })
