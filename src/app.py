from aiohttp import web
from .routes import setup_routes
from loguru import logger
from .logger import run_logger

run_logger()


@logger.catch
async def create_app():
    app = web.Application()
    setup_routes(app)
    logger.info('main app start')
    return app
