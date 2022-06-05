from ..connection.connection import create_connection
from sqlite3 import Error


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class TableVars:
    """
    This is the class for defining the tables
    """

    sql_create_images_table = """CREATE TABLE IF NOT EXISTS images (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            url text NOT NULL,
                                            height text NOT NULL,
                                            width text NOT NULL
                                        );"""

    sql_create_artists_table = """CREATE TABLE IF NOT EXISTS artists (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                name text NOT NULL,
                                                href text NOT NULL,
                                                type text NOT NULL,
                                                image_id integer,
                                                uri text NOT NULL,
                                                popularity integer,
                                                FOREIGN KEY (image_id) REFERENCES images (id)
                                            );"""

    sql_create_items_table = """CREATE TABLE IF NOT EXISTS items (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                name text NOT NULL,
                                                href text NOT NULL
                                            );"""

    sql_create_tracks_table = """CREATE TABLE IF NOT EXISTS tracks (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                "limit" integer NOT NULL,
                                                href text NOT NULL,
                                                next text NOT NULL,
                                                offset integer NOT NULL,
                                                previous text NOT NULL,
                                                total integer NOT NULL
                                            );"""

    sql_create_albums_table = """CREATE TABLE IF NOT EXISTS albums (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        album_type text NOT NULL,
                                        name text NOT NULL,
                                        release_date text NOT NULL,
                                        type text NOT NULL,
                                        uri text NOT NULL,
                                        href text,
                                        available_markets JSON DEFAULT('[]'),
                                        image_id integer NOT NULL,
                                        artist_id integer NOT NULL,
                                        track_id integer NOT NULL,
                                        FOREIGN KEY (image_id) REFERENCES images (id),
                                        FOREIGN KEY (artist_id) REFERENCES artists (id),
                                        FOREIGN KEY (track_id) REFERENCES tracks (id)
                                    ); """


def get_table_data(conn, get_query):
    """
    This is to insert the value to the tables
    :param conn: connection object
    :param insert_query: query for the insert
    :return:
    """
    try:
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(get_query)
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)
        return '{}'.format(str(e))


def remove_table_entry(conn, get_query):
    """
    This is to insert the value to the tables
    :param conn: connection object
    :param insert_query: query for the insert
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(get_query)
    except Error as e:
        print(e)
        return '{}'.format(str(e))


def insert_table(conn, insert_query, data):
    """
    This is to insert the value to the tables
    :param conn: connection object
    :param insert_query: query for the insert
    :return:
    """
    try:

        c = conn.cursor()
        c.execute(insert_query, data)
        print(c)
        conn.commit()
        c.close()
        return True
    except Error as e:
        print(e)
        return '{}'.format(str(e))


def create_table(conn, table_name):
    """ This is to create the table for the connection
    :param conn: Connection object for the application
    :param table_name: a CREATE TABLE
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(table_name)
        print(c)
    except Error as e:
        print(e)


def create_db_conn():
    """
    This function generates creates the table by setting the connections for the different tables
    """
    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create images table
        create_table(conn, TableVars.sql_create_images_table)

        # create artists table
        create_table(conn, TableVars.sql_create_artists_table)

        # create items table
        create_table(conn, TableVars.sql_create_items_table)

        # create tracks table
        create_table(conn, TableVars.sql_create_tracks_table)

        # create albums table
        create_table(conn, TableVars.sql_create_albums_table)

        return True
    else:
        print("Error! cannot create the database connection.")
        return False
