from chilo_api.core.logger.common import CommonLogger


def log(**kwargs):
    try:
        logger = CommonLogger(**kwargs)
        logger.log(**kwargs)
    except Exception as exception:
        raise RuntimeError(exception) from exception
