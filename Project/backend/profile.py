from flask import Blueprint, request, jsonify   #type:ignore
from backend.database import get_db

profile = Blueprint("profile",__name__)

# CREATE PROFILE
@profile.route("/profile", methods=["POST"])
def create_profile():
    data=request.json
    username=data["username"]
    email=data["email"]
    phone=data["phone"]

    conn=get_db()
    cursor=conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS profiles(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,email TEXT,phone TEXT)""")

    cursor.execute("INSERT INTO profiles(username,email,phone) VALUES(?,?,?)",(username,email,phone))

    conn.commit()
    conn.close()

    return jsonify({"message":"Profile created"})

# UPDATE PROFILE
@profile.route("/profile/update", methods=["PUT"])
def update_profile():
    data=request.json
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("""UPDATE profiles SET email=?, phone=? WHERE username=?""",(data["email"],data["phone"],data["username"]))

    conn.commit()
    conn.close()

    return jsonify({"message":"Profile updated"})

# DELETE PROFILE
@profile.route("/profile/delete", methods=["DELETE"])
def delete_profile():
    data=request.json
    conn=get_db()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM profiles WHERE username=?",(data["username"],))

    conn.commit()
    conn.close()
    
    return jsonify({
    "message":"Profile deleted"})