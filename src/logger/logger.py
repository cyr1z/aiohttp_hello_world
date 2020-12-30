from dotenv import dotenv_values

from loguru import logger

from src.logger.logger_settings import FORMAT, ROTATION, CHANNELS, \
    DEFAULT_LEVEL, COMPRESSION, COLORIZE_DEFAULT, SERIALIZE_DEFAULT, \
    DIAGNOSE_DEFAULT, BACKTRACE_DEFAULT, ENQUEUE_DEFAULT

config = dotenv_values(".env")


def run_logger():
    """
    Start all channels from logger_settings.CHANNELS
    """
    for channel in CHANNELS:

        log_level = channel.get('level', DEFAULT_LEVEL)

        # set prod loglevel on production instance
        if config.get('PROD'):
            log_level = channel.get('prod_level', DEFAULT_LEVEL)

        # get arguments from settings
        arguments = {'format': channel.get('format', FORMAT),
                     'level': log_level,
                     'colorize': channel.get('colorize', COLORIZE_DEFAULT),
                     'serialize': channel.get('serialize', SERIALIZE_DEFAULT),
                     'diagnose': channel.get('diagnose', DIAGNOSE_DEFAULT),
                     'backtrace': channel.get('backtrace', BACKTRACE_DEFAULT)}

        # std.err and std.out do not have the following parameters
        if isinstance(channel.get('channel'), str):
            arguments.update(
                {
                    'enqueue': channel.get('enqueue', ENQUEUE_DEFAULT),
                    'compression': channel.get('compression', COMPRESSION),
                    'rotation': channel.get('rotation', ROTATION),
                }
            )

        logger.add(channel.get('channel'), **arguments)
