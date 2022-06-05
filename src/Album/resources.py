from flask import Blueprint
from flask import request
from flask_jwt import jwt_required
import sqlite3
from flask import make_response, jsonify
from ..db.sql import create_db_conn, insert_table, get_table_data, remove_table_entry
from ..connection.connection import create_connection
bp = Blueprint('pos', __name__, url_prefix='/api/v1')


@bp.route("/create_tables", methods=['POST'])
def create_tables():
    tables = create_db_conn()
    if tables:
        return make_response(jsonify({'message': 'Tables created successfully', 'status': 200}), 200)
    else:
        return make_response(jsonify({'message': 'Tables not created properly', 'status': 422}), 422)


@bp.route("/insert_images", methods=['POST'])
def insert_images():
    data = request.json
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    if not data:
        return make_response(jsonify({"message": "Please data is not inserted", "status": 401}), 401)
    if 'url' not in data:
        return make_response(jsonify({"message": "url is required", "status": 401}), 401)
    if 'height' not in data:
        return make_response(jsonify({"message": "height is required", "status": 401}), 401)
    if 'width' not in data:
        return make_response(jsonify({"message": "weight is required", "status": 401}), 401)
    conn = create_connection()
    try:
        sqlite_insert_with_param = """INSERT INTO images
                              (url, height, width) 
                              VALUES (?, ?, ?);"""

        data_tuple = (data['url'], data['height'], data['width'])
        inserted = insert_table(conn, sqlite_insert_with_param, data_tuple)
        if inserted:
            return make_response(jsonify({"message": 'Data inserted for images successfully', "status": 200})), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/insert_artists", methods=['POST'])
def insert_artists():
    data = request.json
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    if not data:
        return make_response(jsonify({"message": "Please data is not inserted", "status": 401}), 401)
    if 'name' not in data:
        return make_response(jsonify({"message": "name is required", "status": 401}), 401)
    if 'href' not in data:
        return make_response(jsonify({"message": "href is required", "status": 401}), 401)
    if 'type' not in data:
        return make_response(jsonify({"message": "type is required", "status": 401}), 401)
    if 'uri' not in data:
        return make_response(jsonify({"message": "uri is required", "status": 401}), 401)
    if 'image_id' not in data:
        return make_response(jsonify({"message": "image_id is required", "status": 401}), 401)
    if 'popularity' not in data:
        return make_response(jsonify({"message": "popularity is required", "status": 401}), 401)
    conn = create_connection()
    try:
        sqlite_insert_with_param = """INSERT INTO artists
                              (name, href, type, uri, image_id, popularity) 
                              VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (data['name'], data['href'], data['type'], data['uri'], data['image_id'], int(data['popularity']))
        inserted = insert_table(conn, sqlite_insert_with_param, data_tuple)
        if inserted:
            return make_response(jsonify({"message": 'Data inserted for artists successfully', "status": 200})), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/insert_items", methods=['POST'])
def insert_items():
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    data = request.json
    if not data:
        return make_response(jsonify({"message": "Please data is not inserted", "status": 401}), 401)
    if 'name' not in data:
        return make_response(jsonify({"message": "name is required", "status": 401}), 401)
    if 'href' not in data:
        return make_response(jsonify({"message": "href is required", "status": 401}), 401)
    conn = create_connection()
    try:
        sqlite_insert_with_param = """INSERT INTO items
                              (name, href) 
                              VALUES (?, ?);"""

        data_tuple = (data['name'], data['href'])
        inserted = insert_table(conn, sqlite_insert_with_param, data_tuple)
        if inserted:
            return make_response(jsonify({"message": 'Data inserted for items successfully', "status": 200})), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/insert_tracks", methods=['POST'])
def insert_tracks():
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    data = request.json
    if not data:
        return make_response(jsonify({"message": "Please data is not inserted", "status": 401}), 401)
    if 'limit' not in data:
        return make_response(jsonify({"message": "limit is required", "status": 401}), 401)
    if 'href' not in data:
        return make_response(jsonify({"message": "href is required", "status": 401}), 401)
    if 'next' not in data:
        return make_response(jsonify({"message": "next is required", "status": 401}), 401)
    if 'offset' not in data:
        return make_response(jsonify({"message": "offset is required", "status": 401}), 401)
    if 'previous' not in data:
        return make_response(jsonify({"message": "previous is required", "status": 401}), 401)
    if 'total' not in data:
        return make_response(jsonify({"message": "total is required", "status": 401}), 401)
    conn = create_connection()
    try:
        sqlite_insert_with_param = """INSERT INTO tracks
                              ("limit", href, next, offset, previous, total) 
                              VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (int(data['limit']), data['href'], data['next'], int(data['offset']), data['previous'],
                      int(data['total']))
        inserted = insert_table(conn, sqlite_insert_with_param, data_tuple)
        if inserted:
            return make_response(jsonify({"message": 'Data inserted for tracks successfully', "status": 200})), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/insert_albums", methods=['POST'])
def insert_albums():
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    data = request.json
    if not data:
        return make_response(jsonify({"message": "Please data is not inserted", "status": 401}), 401)
    if 'album_type' not in data:
        return make_response(jsonify({"message": "album_type is required", "status": 401}), 401)
    if 'name' not in data:
        return make_response(jsonify({"message": "name is required", "status": 401}), 401)
    if 'release_date' not in data:
        return make_response(jsonify({"message": "release_date is required", "status": 401}), 401)
    if 'type' not in data:
        return make_response(jsonify({"message": "type is required", "status": 401}), 401)
    if 'uri' not in data:
        return make_response(jsonify({"message": "uri is required", "status": 401}), 401)
    if 'href' not in data:
        return make_response(jsonify({"message": "href is required", "status": 401}), 401)
    if 'available_markets' not in data:
        return make_response(jsonify({"message": "available_markets is required", "status": 401}), 401)
    if 'image_id' not in data:
        return make_response(jsonify({"message": "image_id is required", "status": 401}), 401)
    if 'artist_id' not in data:
        return make_response(jsonify({"message": "artist_id is required", "status": 401}), 401)
    if 'track_id' not in data:
        return make_response(jsonify({"message": "track_id is required", "status": 401}), 401)
    conn = create_connection()
    try:
        sqlite_insert_with_param = """INSERT INTO albums
                              (album_type, name, release_date, type, uri, href, available_markets, image_id,
                               artist_id, track_id) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (data['album_type'], data['name'], data['release_date'], data['type'], data['uri'], data['href'],
                      data['available_markets'], data['image_id'], data['artist_id'], data['track_id'])
        inserted = insert_table(conn, sqlite_insert_with_param, data_tuple)
        if inserted:
            return make_response(jsonify({"message": 'Data inserted for tracks successfully', "status": 200})), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/get_images", methods=['GET'])
@bp.route("/get_images/<id>", methods=['GET'])
def get_images(id=None):
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    conn = create_connection()
    try:
        if id:
            sqlite_get_with_param = "SELECT * FROM images WHERE id={};".format(id)
        else:
            sqlite_get_with_param = "SELECT * FROM images;"

        inserted = get_table_data(conn, sqlite_get_with_param)
        for row in inserted:
            print(row)
        if inserted:
            return make_response(jsonify(inserted)), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/get_artists", methods=['GET'])
@bp.route("/get_artists/<id>", methods=['GET'])
def get_artists(id=None):
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    conn = create_connection()
    try:
        if id:
            sqlite_get_with_param = "SELECT * FROM artists WHERE id={};".format(id)
        else:
            sqlite_get_with_param = "SELECT * FROM artists;"

        inserted = get_table_data(conn, sqlite_get_with_param)
        if inserted:
            return make_response(jsonify(inserted)), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/get_albums", methods=['GET'])
@bp.route("/get_albums/<id>", methods=['GET'])
def get_albums(id=None):
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    conn = create_connection()
    try:
        if id:
            sqlite_get_with_param = "SELECT * FROM albums WHERE id={};".format(id)
        else:
            sqlite_get_with_param = "SELECT * FROM albums;"

        inserted = get_table_data(conn, sqlite_get_with_param)
        if inserted:
            return make_response(jsonify(inserted)), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/get_album_tracks", methods=['GET'])
@bp.route("/get_album_tracks/<id>/tracks", methods=['GET'])
def get_album_track(id=None):
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    data = request.args
    limit = None
    offset = None
    if 'limit' in data:
        limit = data['limit']
    if 'offset' in data:
        offset = data['offset']
    conn = create_connection()
    try:
        if id:
            if limit and offset:
                sqlite_get_with_param = "SELECT * FROM tracks WHERE id={} and limit= {} and offset= {};".format(id,
                                                                                                                limit,
                                                                                                                offset)
            else:
                sqlite_get_with_param = "SELECT * FROM tracks WHERE id={};".format(id)
        else:
            if limit and offset:
                sqlite_get_with_param = 'SELECT * FROM tracks WHERE "limit"= {} and offset= {};'.format(limit, offset)
            else:
                sqlite_get_with_param = "SELECT * FROM tracks;"

        inserted = get_table_data(conn, sqlite_get_with_param)
        if inserted:
            return make_response(jsonify(inserted)), 200
        else:
            return make_response(jsonify({"message": str(inserted), "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


@bp.route("/delete_album/<id>", methods=['DELETE'])
def delete_album(id=None):
    args = request.environ
    if 'HTTP_AUTHORIZATION' not in args:
        return make_response(jsonify({"message": "Authorization token is missing", "status": 401}), 401)
    conn = create_connection()
    try:
        if id:
            sqlite_get_with_param = "DELETE FROM albums WHERE id={};".format(id)

            inserted = remove_table_entry(conn, sqlite_get_with_param)
            if inserted:
                return make_response(jsonify(inserted)), 200
            else:
                return make_response(jsonify({"message": "No data found", "status": 422})), 422
        else:
            return make_response(jsonify({"message": "Please specify the id for deletion", "status": 422})), 422

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")



