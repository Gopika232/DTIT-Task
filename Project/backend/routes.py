from flask import Blueprint, request, jsonify    #type:ignore
from backend.auth import login, register
from models.prediction import predictor
from backend.database import get_db
from models.model import model
from datetime import datetime
import csv
import os

routes = Blueprint("routes",__name__)

@routes.route("/register",methods=["POST"])
def user_register():
    data=request.json
    result = register(data["username"],data["password"])

    if result:
        return jsonify({
            "message":"Registered successfully"
        })
    
    return jsonify({"message":"Username Already Exists"})


@routes.route("/predict_attendance")
def predict_attendance():

    days = request.args.get("days")

    result = predictor.predict(
        int(days)
    )


    return jsonify({
        "prediction":result
    })

@routes.route("/login",methods=["POST"])
def user_login():
    data=request.json
    result=login(data["username"],data["password"])
    if result:
        return jsonify({"message":"Login success"})

    return jsonify({"message":"Invalid login"})

@routes.route("/attendance")
def attendance():

    conn=get_db()
    cursor=conn.cursor()

    cursor.execute(
    "SELECT * FROM attendance"
    )

    data=cursor.fetchall()

    return jsonify(data)

@routes.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]

    path = "dataset/" + image.filename
    image.save(path)
    result = model.detect_face(path)

    if result["status"] == "Face detected":
        username = request.form.get("username")

        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")

        # store in database
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO attendance(username,date,status) VALUES(?,?,?)""",(username, date, "Present"))

        conn.commit()
        conn.close()

        # store in csv
        file_exists = os.path.isfile("attendance/attendance.csv")

        with open("attendance/attendance.csv","a",newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(
                    ["username","date","time","status"])
            writer.writerow([username,date,time,"Present"])
        return jsonify({
            "message":"Attendance marked",
            "user":username
        })