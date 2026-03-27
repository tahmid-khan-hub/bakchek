import logging
import sys
from app.config import settings

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("bakchek")

    if logger.handlers:
        return logger

    logger.setLevel (
        logging.DEBUG if settings.APP_ENV == "development" else logging.INFO
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter (
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

logger = setup_logger()