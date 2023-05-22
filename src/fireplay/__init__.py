# from fireplay.mp3.service import Mp3
import logging

from fireplay.library.service import MediaLibrary
from fireplay.services import configure_logging, media_libary_service

configure_logging()


def main():
    mp3 = media_libary_service()
    mp3.build_music_list(search_path="/Volumes/DropboxData/Music")
