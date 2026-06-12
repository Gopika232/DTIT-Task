import pandas as pd
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.linear_model import LogisticRegression     #type:ignore
from sklearn.ensemble import RandomForestClassifier     #type:ignore
from sklearn.metrics import accuracy_score      #type:ignore

# Dataset

data = {"Age":[22,25,28,30,35,40,45,50],"Salary":[25000,30000,40000,50000,60000,80000,90000,100000],"Purchased":[0,0,0,1,1,1,1,1]}
df = pd.DataFrame(data)

X = df[["Age","Salary"]]
y = df["Purchased"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# Baseline Model
logistic_model = LogisticRegression()
logistic_model.fit(X_train,y_train)
logistic_prediction = logistic_model.predict(X_test)
baseline_accuracy = accuracy_score(y_test,logistic_prediction)

print("Logistic Regression Accuracy:")
print(baseline_accuracy)

# Ensemble Model
rf_model = RandomForestClassifier(n_estimators=100,random_state=42)

rf_model.fit(X_train,y_train)

rf_prediction = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test,rf_prediction)

print("\nRandom Forest Accuracy:")
print(rf_accuracy)

# Comparison
if rf_accuracy > baseline_accuracy:
    print("\nRandom Forest performed better")
else:
    print("\nLogistic Regression performed better")


####    OUTPUT    ####

# Logistic Regression Accuracy:
# 1.0

# Random Forest Accuracy:
# 1.0

# Logistic Regression performed better