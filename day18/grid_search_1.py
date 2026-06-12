import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV         #type:ignore
from sklearn.linear_model import LogisticRegression    #type:ignore
from sklearn.metrics import accuracy_score    #type:ignore


# Dataset
data = {
    "Age":[22,25,28,30,35,40,45,50,55,60,32,38],
    "Salary":[25000,30000,40000,50000,60000,80000,90000,100000,120000,150000,45000,70000],
    "Purchased":[0,0,0,1,1,1,1,1,1,1,0,1]}

df = pd.DataFrame(data)

# Features and Target
X = df[["Age","Salary"]]
y = df["Purchased"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# Logistic Regression
model = LogisticRegression()

# Hyperparameter Grid
param_grid = {"C": [0.1,1,10],"solver": ["liblinear"]}

# Grid SearcH
grid = GridSearchCV(model,param_grid,cv=2)
grid.fit(X_train,y_train)

print("Best Parameters:")
print(grid.best_params_)

# Prediction
prediction = grid.predict(X_test)
print("\nAccuracy:")
print(accuracy_score(y_test,prediction))

####    OUTPUT  ####

# Best Parameters:
# {'C': 1, 'solver': 'liblinear'}

# Accuracy:
# 1.0