"""
logger.py
--------------------------
Logging System
"""

import logging
from pathlib import Path

Path("data").mkdir(exist_ok=True)

logging.basicConfig(

    filename="data/app.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)


class AppLogger:

    @staticmethod
    def info(message):

        logging.info(message)

    @staticmethod
    def warning(message):

        logging.warning(message)

    @staticmethod
    def error(message):

        logging.error(message)

    @staticmethod
    def exception(message):

        logging.exception(message)