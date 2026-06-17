from flask import request, jsonify    #type:ignore
from functools import wraps
from backend.database import get_db

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.headers.get("username")
        if not username:
            return jsonify({"message":"Unauthorized"}),401
        return func(*args, **kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.headers.get("username")

        if not username:
            return jsonify({"message":"Unauthorized"}),401

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT role FROM users WHERE username=?",(username,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return jsonify({"message":"User not found"}),404

        if user[0] != "admin":
            return jsonify({"message":"Admin access required"}),403
        return func(*args, **kwargs)
    return wrapper