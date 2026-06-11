from sklearn.datasets import load_iris  #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
import joblib  #type:ignore


# Load dataset
data = load_iris()

X = data.data
y = data.target


# Train model
model = RandomForestClassifier()

model.fit(X,y)


# Save model
joblib.dump(model,"attendance_model.pkl")
print("Model saved successfully")