# from fireplay.mp3.service import Mp3
import logging

from fireplay.library.service import MediaLibrary
from fireplay.services import configure_logging, cursor, init_tables


def main():
    configure_logging()
    con, db = cursor()
    mp3 = MediaLibrary(db, con)
    mp3.build_music_list(search_path="/Volumes/DropboxData/Music")
