from sklearn.datasets import load_iris  #type:ignore
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.svm import SVC  #type:ignore
import joblib   #type:ignore
import pandas as pd

# Load dataset
data = load_iris()

X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train model
model = SVC()
model.fit(X_train, y_train)


# Save model
joblib.dump(model, "model.pkl")
print("Model saved successfully")

# Load model
loaded_model = joblib.load("model.pkl")

# Prediction
result = loaded_model.predict([[5.1, 3.5, 1.4, 0.2]])

print("Prediction:", result)













































































































































