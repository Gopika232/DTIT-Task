from flask import Flask, request, jsonify #type:ignore
import joblib  #type:ignore

app = Flask(__name__)

model = joblib.load("attendance_model.pkl")

@app.route("/")
def home():
    return "AI Attendance System Flask API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = model.predict([data["features"]])

    return jsonify({"prediction": int(result[0])})
if __name__ == "__main__":
    app.run(debug=True)