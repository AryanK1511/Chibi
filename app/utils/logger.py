import logging


def setup_logging():
    logger = logging.getLogger("uvicorn")
    return logger


logger = setup_logging()
