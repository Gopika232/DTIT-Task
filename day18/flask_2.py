from flask import Flask, request, jsonify   #type:ignore
import joblib  #type:ignore

app = Flask(__name__)

# Load trained model
model = joblib.load("iris_model.pkl")
@app.route("/")
def home():
    return "ML Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})
if __name__ == "__main__":
    app.run(debug=True)