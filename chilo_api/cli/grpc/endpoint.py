import json


class GRPCEndpoint:

    def __init__(self, **kwargs):
        self.__rpc = kwargs['rpc']
        self.__rpc_func_name = kwargs['rpc_func_name']
        self.__requirements  = kwargs['requirements']
        self.__protobuf = self.__requirements['protobuf']
        self.__package_identifier = ''
        self.__pb2_module = None
        self.__pb2_grpc_module = None
        self.__service_name = ''
        self.__response_func_name = ''
        self.__request_stream = False
        self.__response_stream = False

    @classmethod
    def get_endpoints_from_modules(cls, modules):
        endpoints = []
        for module in modules:
            rpcs = [function for function in dir(module) if function and function.startswith('rpc_')]
            for rpc in rpcs:
                rpc_func = getattr(module, rpc)
                endpoint = cls(
                    rpc_func_name=rpc,
                    rpc=rpc_func,
                    requirements=getattr(rpc_func, 'requirements')
                )
                endpoints.append(endpoint)
        return endpoints

    @property
    def rpc_func_name(self):
        return self.__rpc_func_name

    @property
    def rpc_name(self):
        clean_space = self.rpc_func_name.split('rpc_')[1]
        temp = clean_space.split('_')
        return ''.join(ele.title() for ele in temp)

    @property
    def rpc(self):
        return self.__rpc

    @property
    def requirements(self):
        return self.__requirements

    @property
    def protobuf(self):
        return self.__protobuf

    @property
    def package_identifier(self):
        return self.__package_identifier

    @package_identifier.setter
    def package_identifier(self, package_identifier):
        self.__package_identifier = package_identifier

    @property
    def pb2_file(self):
        return f'{self.__package_identifier}_pb2'

    @property
    def pb2_grpc_file(self):
        return f'{self.__package_identifier}_pb2_grpc'
    
    @property
    def pb2_module(self):
        return self.__pb2_module

    @pb2_module.setter
    def pb2_module(self, pb2_module):
        self.__pb2_module = pb2_module

    @property
    def pb2_grpc_module(self):
        return self.__pb2_grpc_module

    @pb2_grpc_module.setter
    def pb2_grpc_module(self, pb2_grpc_module):
        self.__pb2_grpc_module = pb2_grpc_module
    
    @property
    def service_name(self):
        return self.__service_name

    @service_name.setter
    def service_name(self, service_name):
        self.__service_name = service_name
    
    @property
    def servicer_name(self):
        return f'{self.service_name}Servicer'

    @property
    def response_func_name(self):
        return self.__response_func_name

    @response_func_name.setter
    def response_func_name(self, response_func_name):
        self.__response_func_name = response_func_name
    
    @property
    def request_stream(self):
        return self.__request_stream

    @request_stream.setter
    def request_stream(self, request_stream):
        self.__request_stream = request_stream
    
    @property
    def response_stream(self):
        return self.__response_stream

    @response_stream.setter
    def response_stream(self, response_stream):
        self.__response_stream = response_stream

    def __str__(self):
        return json.dumps({
            'rpc_func_name': self.rpc_func_name,
            'rpc_name': self.rpc_name,
            'requirements': self.requirements,
            'protobuf': self.protobuf,
            'package_identifier': self.package_identifier,
            'pb2_file': self.pb2_file,
            'pb2_grpc_file': self.pb2_grpc_file,
            'service_name': self.service_name,
            'servicer_name': self.servicer_name,
            'response_func_name': self.response_func_name,
            'request_stream': self.request_stream,
            'response_stream': self.response_stream
        })
