import sqlite3

import pytest
from fireplay.library.service import MediaLibrary

def test_create_instance_media_library():

    conn = sqlite3.connect("foo.db")
    cursor = conn.cursor()

    instance = MediaLibrary(conn, cursor)

    assert isinstance(instance, MediaLibrary)