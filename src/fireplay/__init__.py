# from fireplay.mp3.service import Mp3
import logging

from fireplay.mp3.service import Mp3
from fireplay.services import init_tables, cursor, configure_logging


def main():
    configure_logging()
    logging.debug("I am in main")
    # files = Mp3.build_music_list(search_path="/Volumes/DropboxData/Music")
    con, db = cursor()
    # init_tables(db)
    mp3 = Mp3(db, con)
    files = mp3.build_music_list(search_path="/Volumes/DropboxData/Music")