import sys

FORMAT = '{time} {level} {message}'
ROTATION = '1 week'
DEFAULT_LEVEL = 'WARNING'
COMPRESSION = 'zip'

CHANNELS = [
    {
        'channel': 'logfile.json',
        'format': FORMAT,
        'level': 'DEBUG',
        'prod_level': 'WARNING',
        'compression': COMPRESSION,
        'colorize': False,
        'serialize': True,
        'diagnose': False,
        'backtrace': False,
        'enqueue': True,
        'rotation': ROTATION,

    },
    {
        'channel': 'logfile.log',
        'level': 'DEBUG',
        'rotation': ROTATION,
    },
    {
        'channel': sys.stdout,
        'level': 'DEBUG',
        'colorize': True,
        'diagnose': True,
        'backtrace': True,

    },
    {
        'channel': sys.stderr,
        'level': 'ERROR',
        'colorize': True,
        'diagnose': True,
        'backtrace': True,

    },
]
