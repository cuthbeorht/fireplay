from __future__ import annotations

import json
from typing import Optional

from pydantic import BaseModel
import subprocess
from pathlib import Path

# Taken from the Wikipedia definition of an MP3 file
# https://en.wikipedia.org/wiki/MP3#/media/File:Mp3filestructure.svg
class MediaProperties:
    """

    """

    file_name: str
    """
    Name of the file found on the disk
    """

    format_name: str
    """
    Name of the encoded format
    """

    codec_type: str
    """
    Codec used to encode the media
    """

    encoder_name: str
    """
    Name of the encoder used
    """

    size: int
    """
    Total size in bytes of the media
    """

    artist: Optional[str]
    """
    Name of the artist
    """

    title: str
    """
    Title of the media
    """

    genre: str
    """
    Category of media
    """

    comment: Optional[str]
    """
    Any extra description for the media
    """

    @classmethod
    def from_file(cls, media_file: Path) -> MediaProperties:

        media = cls()

        output = subprocess.run(['ffprobe', '-hide_banner', '-loglevel', 'fatal', '-show_error',  '-show_format',  '-show_streams',  '-show_programs',  '-show_chapters', '-show_private_data', '-print_format', 'json', str(media_file)], capture_output=True)
        media_object = json.loads(output.stdout)

        media.file_name = media_object['format']['filename']
        media.format_name = media_object['format']['format_name']
        media.codec_type = media_object['streams'][0]['codec_type']
        media.encoder_name = media_object['streams'][0]['tags']['encoder']
        media.size = int(media_object['format']['size'])
        media.artist = media_object['format']['tags']['artist']
        media.title = media_object['format']['tags']['title']
        media.genre = media_object['format']['tags']['genre']
        media.comment = media_object['format']['tags']['comment']

        return media
