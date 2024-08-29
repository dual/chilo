import json


class GRPCEndpoint:

    def __init__(self, **kwargs):
        self.__rpc = kwargs['rpc']
        self.__rpc_func_name = kwargs['rpc_func_name']
        self.__requirements  = kwargs['requirements']
        self.__protobuf = self.__requirements['protobuf']

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

    def __str__(self):
        return json.dumps({
            'rpc_func_name': self.rpc_func_name,
            'rpc_name': self.rpc_name,
            'requirements': self.requirements,
            'protobuf': self.protobuf
        })