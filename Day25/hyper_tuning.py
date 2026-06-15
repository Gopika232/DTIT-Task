import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV   #type:ignore
from sklearn.ensemble import RandomForestClassifier      #type:ignore
from sklearn.datasets import load_iris      #type:ignore
from sklearn.metrics import accuracy_score            #type:ignore


# Load dataset
data = load_iris()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()

# Parameters to tune
param_grid = {'n_estimators': [50, 100, 150],'max_depth': [3, 5, 10]}

# Grid Search
grid = GridSearchCV(estimator=model,param_grid=param_grid,cv=3)

grid.fit(X_train, y_train)

# Best parameters
print("Best Parameters:")
print(grid.best_params_)

# Prediction
y_pred = grid.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))


####     OUTPUT    ####

# Best Parameters:
# {'max_depth': 5, 'n_estimators': 50}
# Accuracy:
# 1.0