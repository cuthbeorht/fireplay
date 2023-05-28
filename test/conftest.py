import os.path
from pathlib import Path

import pytest


@pytest.fixture()
def valid_sample_media_files_path() -> Path:
    return Path(os.path.abspath("test/fixtures"))

@pytest.fixture()
def valid_sample_mp3() -> Path:
    return Path(os.path.abspath("test/fixtures/Weekend.mp3"))
