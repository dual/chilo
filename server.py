from werkzeug.serving import run_simple
from chilo import Chilo

api_server = Chilo(
    base_path='/',
    handlers='tests/mocks/handlers',
)


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, api_server.route)
