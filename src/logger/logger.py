import _io
import sys

from dotenv import dotenv_values

from loguru import logger

from src.logger.logger_settings import FORMAT, ROTATION, CHANNELS, \
    DEFAULT_LEVEL, COMPRESSION

config = dotenv_values(".env")


def run_logger():
    for channel in CHANNELS:

        log_level = channel.get('level', DEFAULT_LEVEL)
        if config.get('PROD'):
            log_level = channel.get('prod_level', DEFAULT_LEVEL)

        arguments = {'format': channel.get('format', FORMAT),
                     'level': log_level,
                     'colorize': channel.get('colorize', False),
                     'serialize': channel.get('serialize', False),
                     'diagnose': channel.get('diagnose', False),
                     'backtrace': channel.get('backtrace', False)}
        if isinstance(channel.get('channel'), str):
            arguments.update({
                'enqueue': channel.get('enqueue', True),
                'compression': channel.get('compression', COMPRESSION),
            })
        logger.add(channel.get('channel'), **arguments)


if __name__ == "__main__":

    @logger.catch
    def zero_dev(x):
        return 1 / (x)


    logger.debug("That's it, beautiful and simple logging!")
    for i in (0, 'b', (12, 9)):
        try:
            zero_dev(i)
        except:
            pass
