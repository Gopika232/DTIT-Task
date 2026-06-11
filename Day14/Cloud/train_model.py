from sklearn.datasets import load_iris  #type:ignore
from sklearn.ensemble import RandomForestClassifier    #type:ignore
import joblib    #type:ignore

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Create model
model = RandomForestClassifier(n_estimators=50,max_depth=5,random_state=42)

# Train
model.fit(X,y)

# Save model
joblib.dump(model,"model.pkl")

print("Model saved successfully")