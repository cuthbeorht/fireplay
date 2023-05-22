import logging
import sqlite3
from typing import List

from fireplay.library.models import MediaLibraryItem


class MediaLibraryRepository:
    """ """

    def __init__(self, connection: sqlite3.Connection):
        """

        :param connection:
        """
        self._connection = connection

    @classmethod
    def init_tables(cls, cursor: sqlite3.Cursor):
        try:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS main.medias (title TEXT, file_name TEXT, size INT, media_type TEXT);"
            )

        except sqlite3.OperationalError as e:
            logging.error(f"Error creating tables: {e}")

    def add(self, media_item: MediaLibraryItem) -> MediaLibraryItem:
        """

        :param media_item:
        :return:
        """

        self._connection.cursor().execute(
            f'INSERT INTO main.medias (title, file_name, size, media_type) VALUES ("{media_item.file_name}", "{media_item.file_name}", {media_item.size}, \'audio/mpeg\');'
        )
        media_item.id = self._connection.cursor().lastrowid

        return media_item

    def find(self, media_item: MediaLibraryItem) -> List[MediaLibraryItem]:
        return (
            self._connection.cursor()
            .execute(
                f'select * from main.medias where file_name = "{media_item.file_name}"'
            )
            .fetchall()
        )
