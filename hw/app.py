from aiohttp import web
import aiohttp_jinja2
from jinja2 import PackageLoader
from .routes import setup_routes


async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=PackageLoader('hw', 'templates')
    )
    setup_routes(app)
    return app
