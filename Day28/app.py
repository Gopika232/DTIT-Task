from flask import Flask, request, jsonify  #type:ignore
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("attendance_model.pkl", "rb"))

@app.route("/")
def home():
    return "ML Model API Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("Received:", data)

        x = data["x"]
        y = data["y"]
        w = data["w"]

        input_data = np.array([[x, y, w]])
        prediction = model.predict(input_data)

        return jsonify({"employee": str(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)