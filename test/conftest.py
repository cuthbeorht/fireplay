import os.path
from pathlib import Path

import pytest


@pytest.fixture()
def valid_sample_media_file() -> Path:
    return Path(os.path.abspath("test/fixtures"))
