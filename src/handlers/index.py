from aiohttp import web


class IndexHandler:
    def __init__(self):
        pass

    async def handler(self, request):
        data = {'text': 'Hello'}
        return web.json_response(data)
