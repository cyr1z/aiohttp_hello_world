from aiohttp import web
from datetime import datetime as dt
from socket import gethostname


class StatusHandler:
    def __init__(self):
        pass

    async def handler(self, request):
        dt_now = dt.now()
        data = {
            'timestamp': dt_now.timestamp(),
            'datetime': dt_now.strftime("%Y-%m-%d %H:%M:%S"),
            'hostname': gethostname()}
        return web.json_response(data)
