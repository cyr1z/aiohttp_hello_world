from aiohttp import web
import asyncio
import async_timeout

from hw import create_app

app = create_app()

if __name__ == '__main__':
    web.run_app(app, )
