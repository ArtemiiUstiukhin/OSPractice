import logging
import sys

from aiohttp import web
from routes import setup_routes
from settings import config

async def init_app(argv=None):
    app = web.Application()

    app['config'] = config

    setup_routes(app)

    return app

def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    web.run_app(app,
                host=config['host'],
                port=config['port'])

if __name__ == '__main__':
    main(sys.argv[1:])