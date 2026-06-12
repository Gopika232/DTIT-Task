import pandas as pd
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.linear_model import LogisticRegression      #type:ignore
from sklearn.metrics import accuracy_score     #type:ignore

# Dataset
data = {
    "Age":[22,25,28,30,35,40,45,50],
    "Salary":[25000,30000,40000,50000,60000,80000,90000,100000],
    "Purchased":[0,0,0,1,1,1,1,1]}

df = pd.DataFrame(data)
X = df[["Age","Salary"]]
y = df["Purchased"]


# Split Data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# Baseline Model
model = LogisticRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)
print("Before Feature Engineering Accuracy:")
print(accuracy_score(y_test,prediction))

# Feature Engineering
X_train["Salary_Age"] = (X_train["Salary"] /X_train["Age"])

X_test["Salary_Age"] = (X_test["Salary"] /X_test["Age"])

# Train with new feature
new_model = LogisticRegression()
new_model.fit(X_train,y_train)

new_prediction = new_model.predict(X_test)
print("\nAfter Feature Engineering Accuracy:")
print(accuracy_score(y_test,new_prediction))

####     OUTPUT      ####
# Before Feature Engineering Accuracy:
# 1.0

# After Feature Engineering Accuracy:
# 1.0