from sklearn.datasets import load_iris   #type:ignore
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.preprocessing import StandardScaler   #type:ignore
from sklearn.linear_model import LogisticRegression    #type:ignore
from sklearn.ensemble import RandomForestClassifier, VotingClassifier    #type:ignore
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report   #type:ignore

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create models
logistic_model = LogisticRegression()
random_forest = RandomForestClassifier(n_estimators=100,random_state=42)

# Create ensemble model
ensemble_model = VotingClassifier(
    estimators=[("lr", logistic_model),("rf", random_forest)],voting="hard")

# Train model
ensemble_model.fit(X_train,y_train)

# Prediction
y_pred = ensemble_model.predict(X_test)

# Evaluation
print("Accuracy:")
print(accuracy_score(y_test,y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))
print("\nClassification Report:")
print(classification_report(y_test,y_pred))




####           OUTPUT      ####

# Accuracy:
# 1.0

# Confusion Matrix:
# [[10  0  0]
#  [ 0  9  0]
#  [ 0  0 11]]

# Classification Report:
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00        10
#            1       1.00      1.00      1.00         9
#            2       1.00      1.00      1.00        11

#     accuracy                           1.00        30
#    macro avg       1.00      1.00      1.00        30
# weighted avg       1.00      1.00      1.00        30