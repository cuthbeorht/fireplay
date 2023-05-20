import sqlite3
import logging
import time

from logging.handlers import RotatingFileHandler

def init_tables(cursor):

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS main.medias (title TEXT, file_name TEXT, size INT, media_type TEXT);")


    except sqlite3.OperationalError as e:
        if not "table medias already exists" == e.args[0]:
            raise e

def cursor() -> (sqlite3.Connection, sqlite3.Cursor):

    conn = sqlite3.connect("media.db")
    cursor = conn.cursor()


    init_tables(cursor)
    conn.commit()

    return (conn, cursor)

def configure_logging():

    log_handler = logging.handlers.RotatingFileHandler(
        filename='logs/application.log',
        backupCount=25,
        maxBytes=1000000,
        mode="a"
    )
    formatter = logging.Formatter(
        '%(asctime)s program_name [%(process)d]: %(message)s',
        '%b %d %H:%M:%S')
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)

