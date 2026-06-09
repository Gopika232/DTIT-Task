from sklearn.datasets import load_iris   #type:ignore
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.ensemble import RandomForestClassifier  #type:ignore
from sklearn.metrics import accuracy_score  #type:ignore

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest model
model = RandomForestClassifier(n_estimators=100,random_state=42)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)




#####   OUTPUT    #####
# Accuracy: 1.0