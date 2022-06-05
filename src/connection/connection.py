import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect('album.db')
        return conn
    except Error as e:
        print(e)

    return conn