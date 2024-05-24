import jsonpickle
from werkzeug.wrappers import Request, Response


def serve(environ, start_response):
    request = Request(environ)
    text = f"Hello {request.args.get('name', 'Paul')}!"
    response = Response(text, mimetype='text/plain')
    jsonpickle.set_preferred_backend('simplejson')
    jsonpickle.set_encoder_options('simplejson', use_decimal=True)
    print(jsonpickle.encode(request, indent=4))
    return response(environ, start_response)
