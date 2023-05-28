from pathlib import Path
from unittest.mock import Mock, AsyncMock

import pytest

from fireplay.library.repository import MediaLibraryRepository
from fireplay.library.service import MediaLibrary


@pytest.fixture()
def media_library_repository() -> MediaLibraryRepository:
    fetch_mock = AsyncMock()
    fetch_mock.fetchall = AsyncMock(return_value=None)

    connect_mock = AsyncMock()
    connect_mock.cursor = AsyncMock(return_value=fetch_mock)

    sqlite_mock = AsyncMock()
    sqlite_mock.connect = AsyncMock(return_value=connect_mock)

    return MediaLibraryRepository(sqlite_mock)


@pytest.fixture()
def media_library() -> MediaLibrary:
    repository = AsyncMock()
    repository.find = AsyncMock(return_value=[])
    repository.add = AsyncMock(return_value=None)

    return MediaLibrary(repository)


def test_create_instance_media_library(
    media_library: MediaLibrary,
):
    assert isinstance(media_library, MediaLibrary)


@pytest.mark.asyncio
async def test_given_valid_audio_file_expect_call_to_database(
    valid_sample_media_files_path: Path, media_library: MediaLibrary
):
    await media_library.build_music_list(str(valid_sample_media_files_path))

    media_library._repository.find.assert_called_once()
    media_library._repository.add.assert_called_once()
