# import jsonpickle
# from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from chilo import Chilo

api_server = Chilo(
    base_path='/',
    handlers='tests/handlers',
)
# jsonpickle.set_preferred_backend('simplejson')
# jsonpickle.set_encoder_options('simplejson', use_decimal=True)

# def serve(environ, start_response):
#     request = Request(environ)
#     text = f"Hello {request.args.get('name', 'Paul')}!"
#     response = Response(text, mimetype='text/plain')
#     print(jsonpickle.encode(request, indent=4))
#     return response(environ, start_response)

if __name__ == '__main__':
    run_simple('localhost', 5000, api_server.route)
