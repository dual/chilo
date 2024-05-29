# import jsonpickle
# from werkzeug.wrappers import Request, Response
# from werkzeug.serving import run_simple


# def serve(environ, start_response):
#     request = Request(environ)
#     text = f"Hello {request.args.get('name', 'Paul')}!"
#     response = Response(text, mimetype='text/plain')
#     jsonpickle.set_preferred_backend('simplejson')
#     jsonpickle.set_encoder_options('simplejson', use_decimal=True)
#     print(jsonpickle.encode(request, indent=4))
#     return response(environ, start_response)

# if __name__ == "__main__":
#     run_simple("127.0.0.1", 5000, serve)
