import logging
import sqlite3
import time
from logging.handlers import RotatingFileHandler

from fireplay import MediaLibrary
from fireplay.library.repository import MediaLibraryRepository


def db_connection() -> sqlite3.Connection:
    return sqlite3.connect("media.db")


def media_library_repository(
    connection: sqlite3.Connection = db_connection(),
) -> MediaLibraryRepository:
    MediaLibraryRepository.init_tables(connection)
    return MediaLibraryRepository(connection=connection)


def media_libary_service(
    repository: MediaLibraryRepository = media_library_repository(),
) -> MediaLibrary:
    return MediaLibrary(repository=repository)


def configure_logging():
    log_handler = logging.handlers.RotatingFileHandler(
        filename="logs/application.log", backupCount=25, maxBytes=1000000, mode="a"
    )
    formatter = logging.Formatter(
        "%(asctime)s fireplay [%(process)d]: %(message)s", "%b %d %H:%M:%S"
    )
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
