from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)


# Dataset

X = [[10,20],[15,25],[20,30],[45,55],[80,90],[85,95],[90,100],[90,105]]
# Binary output
y = [0,0,0,0,1,1,1,1]


# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)


# Model
model = LogisticRegression()


# Training
model.fit(X_train,y_train)


# Prediction
y_pred = model.predict(X_test)


print("Predicted Values:")
print(y_pred)


# Accuracy
print("\nAccuracy:")
print(accuracy_score(y_test,y_pred))


# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))


# Report
print("\nClassification Report:")
print(classification_report(y_test,y_pred))



####    OUTPUT   ####
# Predicted Values:
# [1 0 0]

# Accuracy:
# 1.0

# Confusion Matrix:
# [[2 0]
#  [0 1]]

# Classification Report:
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00         2
#            1       1.00      1.00      1.00         1

#     accuracy                           1.00         3
#    macro avg       1.00      1.00      1.00         3
# weighted avg       1.00      1.00      1.00         3