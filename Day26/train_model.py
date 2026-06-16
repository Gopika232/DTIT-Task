from sklearn.datasets import load_iris   #type:ignore
from sklearn.model_selection import train_test_split    #type:ignore
from sklearn.ensemble import RandomForestClassifier    #type:ignore
import joblib     #type:ignore

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully")