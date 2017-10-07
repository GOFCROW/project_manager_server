from configparser import ConfigParser

from tornado.ioloop import IOLoop

import server


def main():
    config = ConfigParser()
    config.read('settings.ini')
    server.launch_app(config)


if __name__ == '__main__':
    main()
