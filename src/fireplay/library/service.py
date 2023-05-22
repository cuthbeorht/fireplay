import logging
import os
import sqlite3
from typing import Any, Optional

import magic
import mutagen
from magic import from_file

from fireplay.services import cursor


class MediaLibrary:
    def __init__(self, db: sqlite3.Cursor, conn: sqlite3.Connection):
        """

        :param db:
        """
        self._db = db
        self._conn = conn

    def build_music_list(self, search_path: str):
        for root, dirs, files in os.walk(search_path):
            for individual_file in files:
                logging.debug(f"Found file {individual_file}")
                full_file_and_path = os.path.join(root, individual_file)

                if magic.from_file(full_file_and_path, mime=True) == "audio/mpeg":
                    logging.debug(f"File is audio media")
                    self._store_media_file(
                        os.stat(full_file_and_path), full_file_and_path, individual_file
                    )
                    self._conn.commit()

    def _store_media_file(self, file_stats: str, full_file_and_path, file_name):
        media_tags = mutagen.File(full_file_and_path)

        found_song = self._db.execute(
            f'select * from main.medias where file_name = "{file_name}"'
        ).fetchall()

        if len(found_song) > 0:
            self._db.execute(
                f'INSERT INTO main.medias (title, file_name, size, media_type) VALUES ("{file_name}", "{file_name}", {file_stats.st_size}, \'audio/mpeg\');'
            )


class MediaLibraryItem:
    id: Optional[str]
    title: str
    file_name: str
    size: int
    media_type: str
    full_file_and_path: str
