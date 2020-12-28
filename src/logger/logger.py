import sys

from loguru import logger


def run_logger():

    logger.add(
        "logfile.log",
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="1 week",
        compression="zip",
        colorize=False,
        serialize=False,
        diagnose=True,
        backtrace=True,
        enqueue=True,
    )

    logger.add(
        "logger.json",
        rotation="1 week",
        format="{time} {level} {message}",
        level="WARNING",
        compression="zip",
        colorize=False,
        serialize=True,
        diagnose=False,
        backtrace=False,
        enqueue=True,
    )

    logger.add(
        sys.stderr,
        format="{time} {level} {message}",
        filter="my_module",
        level="ERROR",
        colorize=True,
        diagnose=True,
        backtrace=True,
        enqueue=True,
    )

    logger.add(
        sys.stdout,
        format="{time} {level} {message}",
        filter="my_module",
        level="DEBUG",
        colorize=True,
        diagnose=True,
        backtrace=True,
        enqueue=True,
    )


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
