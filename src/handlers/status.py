from aiohttp import web
from datetime import datetime as dt
from socket import gethostname

from loguru import logger


class StatusHandler:
    def __init__(self):
        pass

    @logger.catch
    async def handler(self, request):
        dt_now = dt.now()
        data = {
            'timestamp': dt_now.timestamp(),
            'datetime': dt_now.strftime("%Y-%m-%d %H:%M:%S"),
            'hostname': gethostname()}
        data_for_log = data.copy()
        data_for_log.update({'remote': request.remote, 'path': request.path})
        logger.info(data_for_log)

        return web.json_response(data)
