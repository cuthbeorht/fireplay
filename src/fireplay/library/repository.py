import sqlite3
from typing import List

from fireplay.library.service import MediaLibraryItem


class MediaLibraryRepository:
    """ """

    def __init__(self, connection: sqlite3.Connection):
        """

        :param connection:
        """
        self._connection = connection

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
