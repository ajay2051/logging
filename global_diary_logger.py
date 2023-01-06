"""Global Diary Log Module"""
import logging
import os
from typing import Optional


class GlobalDiaryLogger:
    """Generic Module to log"""
    defautloglevel = 10
    env = os.getenv('GLOBAL_DIARY_LOGS')

    def __init__(self, filename: str, loglevelint: Optional[int] = defautloglevel) -> None:
        """Initializes logger object"""
        self.__filename = f'{filename}.log'
        self.__loglevel = logging.getLevelName(loglevelint)

    def get_logger(self) -> logging:
        """Gets the configured logger object"""
        logger = logging.getLogger(__name__)
        logger.setLevel(self.__loglevel)
        file_handler = logging.FileHandler(os.path.join(self.env, self.__filename))
        logger.addHandler(file_handler)
        formatter = logging.Formatter(' %(asctime)s :: %(levelname)s :: %(message)s')
        file_handler.setFormatter(formatter)
        return logger


if __name__ == '__main__':
    logger = GlobalDiaryLogger('test')
    logs = logger.get_logger()
    logs.info('Hello')
