from flask import Blueprint,jsonify  #type:ignore
from backend.database import get_db

reports = Blueprint("reports",__name__)

@reports.route("/reports",methods=["GET"])
def attendance_report():
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    data=cursor.fetchall()

    conn.close()

    result=[]

    for row in data:
        result.append({ "id":row[0],"username":row[1],"date":row[2],"status":row[3] })
    return jsonify(result)