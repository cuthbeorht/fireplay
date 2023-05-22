import sqlite3
from unittest.mock import Mock

import pytest

from fireplay.library.repository import MediaLibraryRepository
from fireplay.library.service import MediaLibrary


@pytest.fixture()
def media_library_repository() -> MediaLibraryRepository:
    class MockSqliteConnection:
        def curosr(self):
            return None

    sqlite3_mock = Mock(return_value=MockSqliteConnection())
    return MediaLibraryRepository(sqlite3_mock)


def test_create_instance_media_library(
    media_library_repository: MediaLibraryRepository,
):
    instance = MediaLibrary(media_library_repository)

    assert isinstance(instance, MediaLibrary)
