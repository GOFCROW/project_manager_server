
import os
from socket import gethostbyname, gethostname

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

from .routes import HANDLERS
from .controllers import Error404Handler
from .connection import DataBase


def launch_app(config):
    DataBase.set_engine(config['Database']['url'])

    settings = get_settings(config)
    app = Application(
        HANDLERS,
        **settings,
        default_handler_class=Error404Handler
    )
    server_address = config['Server']['address']
    if server_address is None or server_address == '':
        app.listen(int(config['Server']['port']))
        print('running server on  http://' + gethostbyname(gethostname()) + ':' + config['Server']['port'])
        print('running on http://localhost:' + config['Server']['port'] + ' also.')
    else:
        app.listen(int(config['Server']['port']), server_address)
        print('running server on  http://' + config['Server']['address'] + ':' + config['Server']['port'])
    IOLoop.instance().start()


def get_settings(config):
    # temp_path = os.path.join(os.getcwd(), 'server', 'templates')
    return {
        "cookie_secret": config["Server"]["cookie_secret"],
        "debug": True
    }
