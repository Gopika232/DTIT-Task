from flask import Flask, request, jsonify       #type:ignore
from sklearn.linear_model import LogisticRegression   #type:ignore
import numpy as np

app = Flask(__name__)

# Sample training data
X = np.array([[20, 50000],[25, 60000],[30, 80000],[35, 90000]])
y = np.array([0, 0, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data['age']
    salary = data['salary']
    result = model.predict([[age, salary]])
    return jsonify({"prediction": int(result[0])})

if __name__ == "__main__":
    app.run(debug=True)