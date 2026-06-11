from flask import Flask, request, jsonify    #type:ignore
import joblib   #type:ignore

app = Flask(__name__)
# Load model once
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return {"message":"ML API is running"}

@app.route("/predict",methods=["POST"])
def predict():
    try:
        data = request.json
        features = data["features"]
        prediction = model.predict([features])
        return jsonify({"prediction":int(prediction[0])})
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)