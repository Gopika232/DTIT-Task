import pandas as pd
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.preprocessing import LabelEncoder      #type:ignore
from sklearn.ensemble import RandomForestClassifier     #type:ignore
from sklearn.metrics import accuracy_score, classification_report     #type:ignore


# Load data
data = pd.read_csv("customer.csv")


# Convert text columns to numbers
encoder = LabelEncoder()

data["Contract"] = encoder.fit_transform(data["Contract"])
data["Churn"] = encoder.fit_transform(data["Churn"])

# Input and output
X = data.drop("Churn", axis=1)
y = data["Churn"]

# Create training and testing data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Ensemble model
model = RandomForestClassifier(n_estimators=100,random_state=42)

# Train
model.fit(X_train,y_train)

# Predict
prediction = model.predict(X_test)

print("Predicted Values:")
print(prediction)

print("\nAccuracy:")
print(accuracy_score(y_test,prediction))

print("\nClassification Report:")
print(classification_report(y_test,prediction))



####       OUTPUT      ####

# Predicted Values:
# [1 0]

# Accuracy:
# 1.0

# Classification Report:
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00         1
#            1       1.00      1.00      1.00         1

#     accuracy                           1.00         2
#    macro avg       1.00      1.00      1.00         2
# weighted avg       1.00      1.00      1.00         2