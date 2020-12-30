"""
in CHANNELS variables
        'channel': 'logfile.json' -  output
        'format': FORMAT - log record format / '{time} {level} {message}'
        'level': 'DEBUG' - log level on dev
        'prod_level': DEFAULT_LEVEL - log level on prod
        'compression': COMPRESSION - compression for old rotated log files
        'colorize': False - colorize output
        'serialize': True  - serialize log record to json
        'diagnose': False
        'backtrace': False
        'enqueue': True
        'rotation': ROTATION
"""
import sys

FORMAT = '{time} {level} {message}'
ROTATION = '1 week'
DEFAULT_LEVEL = 'WARNING'
COMPRESSION = 'zip'
COLORIZE_DEFAULT = False
SERIALIZE_DEFAULT = False
DIAGNOSE_DEFAULT = False
BACKTRACE_DEFAULT = False
ENQUEUE_DEFAULT = True

CHANNELS = [
    {
        'channel': 'logfile.json',
        'level': 'INFO',
        'serialize': True,

    },
    {
        'channel': 'logfile.log',
        'level': 'DEBUG',
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
