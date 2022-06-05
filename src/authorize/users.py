import json
import os
import jwt
from main import app

from datetime import timedelta, datetime
from werkzeug.security import check_password_hash
from flask import Blueprint
from functools import lru_cache
from flask import request
from ..connection.connection import create_connection
from ..db.sql import get_table_data
import sqlite3
from flask import make_response, jsonify
from flask_jwt import jwt_required
bp = Blueprint('pos', __name__, url_prefix='/api/v1')


@bp.route("/user_login", methods=['POST'])
@jwt_required()
def user_login():
    data = request.json
    if 'user_name' not in data:
        return make_response(jsonify({'message': 'Please enter user_name', 'status': 422}), 422)
    if 'user_password' not in data:
        return make_response(jsonify({'message': 'Please enter user_password', 'status': 422}), 422)

    conn = create_connection()
    exist_user = "SELECT * FROM albums WHERE user_name={};".format(data['user_name'])
    user = get_table_data(conn, exist_user)
    flag = False
    if user:
        for u in user:
            val = check_password_hash(u.password.encode('utf-8'), data['user_password'].encode('utf-8'))
            if val:
                flag = True
        if flag:
            token = jwt.encode({
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, app.config['SECRET_KEY'])

            return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
    else:
        return make_response(jsonify({'message': 'No user found', 'status': 400}), 400)
