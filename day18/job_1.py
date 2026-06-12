import joblib  #type:ignore
from sklearn.datasets import load_iris   #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from sklearn.model_selection import train_test_split    #type:ignore


# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train,y_train)

# Save model
joblib.dump(model,"iris_model.pkl")
print("Model saved successfully")

# Load model
loaded_model = joblib.load("iris_model.pkl")

# Prediction
result = loaded_model.predict([[5.1,3.5,1.4,0.2]])
print("Prediction:", result[0])

####  OUTPUT   ####

# Model saved successfully
# Prediction: 0