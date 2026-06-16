from flask import Flask, request, jsonify      #type:ignore
import joblib    #type:ignore
import logging

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Monitoring setup
logging.basicConfig(filename="model_logs.txt",level=logging.INFO)

@app.route("/")
def home():
    return "AI Model API Running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([data])

    # Log prediction
    logging.info("Input: %s Prediction: %s",data,prediction[0])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)