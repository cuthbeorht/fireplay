import sqlite3


def init_tables(cursor):

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS main.medias (title TEXT, file_name TEXT, size INT, media_type TEXT);")


    except sqlite3.OperationalError as e:
        if not "table medias already exists" == e.args[0]:
            raise e

def cursor() -> (sqlite3.Connection, sqlite3.Cursor):

    conn = sqlite3.connect("media.db")
    cursor = conn.cursor()


    init_tables(cursor)
    conn.commit()

    return (conn, cursor)