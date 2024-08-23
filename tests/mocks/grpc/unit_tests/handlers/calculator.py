from chilo_api import requirements

@requirements(
    protobuf='calculator.proto'
)
def rpc_add(request, response):
    print('here')