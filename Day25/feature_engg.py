import pandas as pd
from sklearn.model_selection import train_test_split    #type:ignore
from sklearn.linear_model import LogisticRegression   #type:ignore
from sklearn.metrics import accuracy_score   #type:ignore
from sklearn.datasets import load_iris     #type:ignore

# Load data
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Create new feature
X['petal_ratio'] = (X['petal length (cm)'] / X['petal width (cm)'])
print("New Features:")
print(X.head())

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy after Feature Engineering:",accuracy_score(y_test, prediction))


####      OUTPUT    ####

# New Features:
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  petal_ratio
# 0                5.1               3.5                1.4               0.2          7.0
# 1                4.9               3.0                1.4               0.2          7.0
# 2                4.7               3.2                1.3               0.2          6.5
# 3                4.6               3.1                1.5               0.2          7.5
# 4                5.0               3.6                1.4               0.2          7.0
# Accuracy after Feature Engineering: 1.0