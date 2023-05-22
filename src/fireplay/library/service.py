import logging
import os
import sqlite3
from typing import Optional

import magic
import mutagen

from fireplay.library.models import MediaLibraryItem
from fireplay.library.repository import MediaLibraryRepository


class MediaLibrary:
    def __init__(self, repository: MediaLibraryRepository):
        """

        :param db:
        """
        self._repository = repository

    def build_music_list(self, search_path: str):
        for root, dirs, files in os.walk(search_path):
            for individual_file in files:
                logging.debug(f"Found file {individual_file}")
                full_file_and_path = os.path.join(root, individual_file)

                if magic.from_file(full_file_and_path, mime=True) == "audio/mpeg":
                    logging.debug(f"File is audio media")
                    media_item = MediaLibraryItem(
                        title=individual_file,
                        file_name=individual_file,
                        size=os.stat(full_file_and_path).st_size,
                        media_type=magic.from_file(full_file_and_path, mime=True),
                        full_file_and_path=full_file_and_path,
                    )
                    found_media = self._repository.find(media_item=media_item)
                    if found_media:
                        self._repository.add(media_item)

    def _store_media_file(self, file_stats: str, full_file_and_path, file_name):
        media_tags = mutagen.File(full_file_and_path)

        found_song = self._repository.find()

        if len(found_song) > 0:
            self._db.execute(
                f'INSERT INTO main.medias (title, file_name, size, media_type) VALUES ("{file_name}", "{file_name}", {file_stats.st_size}, \'audio/mpeg\');'
            )
