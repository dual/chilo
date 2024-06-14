import logging

from chilo.core.logger.common import CommonLogger


def log(**kwargs):
    try:
        logger = CommonLogger()
        logger.log(**kwargs)
    except Exception as exception:
        logging.exception(exception)
