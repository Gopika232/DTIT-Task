from flask import Blueprint,jsonify  #type:ignore

notification = Blueprint("notification",__name__)

@notification.route("/notification/<username>")
def notify(username):
    message = (f"Attendance marked successfully for {username}")
    return jsonify({
        "notification":message
        })