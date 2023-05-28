from pathlib import Path
from typing import Any

import pytest
from fireplay.media.models import MediaProperties


@pytest.fixture()
def mp3_contents_as_bytes(valid_sample_mp3: Path) -> bytes:
    contents: None

    with open(valid_sample_mp3, "rb") as f:
        contents = f.read()

    return str(contents)

def test_given_valid_mp3_expect_valid_header_contents(
        valid_sample_mp3: Path
):
    mp3_file = MediaProperties.from_file(valid_sample_mp3)

    assert mp3_file.file_name == '/Users/davidsciacchettano/src/personal/fireplay/test/fixtures/Weekend.mp3'
    assert mp3_file.format_name == 'mp3'
    assert mp3_file.codec_type == 'audio'
    assert mp3_file.encoder_name == 'LAME3.99r'
    assert mp3_file.size == 3819065
    assert mp3_file.artist == 'LesFM'
    assert mp3_file.title == 'Weekend'
    assert mp3_file.genre == 'Abstract'
