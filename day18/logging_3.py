import logging
import joblib   #type:ignore
from sklearn.datasets import load_iris     #type:ignore
from sklearn.metrics import accuracy_score    #type:ignore
from sklearn.model_selection import train_test_split     #type:ignore


# Logging setup
logging.basicConfig(filename="model_monitor.log",level=logging.INFO,format="%(asctime)s - %(message)s")

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Load model
model = joblib.load("iris_model.pkl")

# Prediction
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test,prediction)

# Log performance
logging.info("Model Accuracy: %s",accuracy)

print("Accuracy:",accuracy)
print("Performance logged successfully")

####    OUTPUT     ####

# Accuracy: 1.0
# Performance logged successfully