from flask import Flask,request,jsonify   #type:ignore
app=Flask(__name__)
employee_schedule=[]

@app.route("/predict_schedule",methods=["POST"])

def predict_schedule():
    data=request.json
    employee=data["employee"]
    availability=data["availability"]
    # AI prediction simulation
    if availability=="morning":
        shift="Morning"
    else:
        shift="Evening"

    result={"employee":employee,"recommended_shift":shift, "status":"AI Generated"}
    employee_schedule.append(result)
    return jsonify(result)

@app.route("/schedule",
methods=["GET"])
def view_schedule():
    return jsonify(employee_schedule)
app.run(port=5000,debug=True)