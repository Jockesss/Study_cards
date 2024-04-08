import logging
import os

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())


class LoggerConfigurator:
    @staticmethod
    def setup_logging():
        for name in ["uvicorn", "uvicorn.error", "fastapi"]:
            logging_logger = logging.getLogger(name)
            logging_logger.handlers = [InterceptHandler()]
            logging_logger.propagate = False

        environment = os.getenv('LOGGER', 'local')
        if environment == 'local':
            logger.add("debug.log", level="DEBUG", rotation="10 MB")
        elif environment == 'dev':
            logger.add("debug.log", level="DEBUG", rotation="10 MB")
        else:
            logger.add("error.log", level="ERROR", rotation="10 MB")
            logger.add("warning.log", level="WARNING", rotation="10 MB")
