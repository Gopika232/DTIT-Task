import pandas as pd
from sklearn.model_selection import train_test_split    #type:ignore
from sklearn.linear_model import LogisticRegression     #type:ignore

# Dataset
data = {"Age": [22, 25, 28, 30, 35, 40],"Salary": [25000, 30000, 40000, 50000, 60000, 80000],"Purchased": [0, 0, 0, 1, 1, 1]}

df = pd.DataFrame(data)
X = df[["Age", "Salary"]]
y = df["Purchased"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train,y_train)

# Prediction
predictions = model.predict(X_test)
print("Predictions:")
print(predictions)


####   OUTPUT  ####

# Predictions:
# [0 0]