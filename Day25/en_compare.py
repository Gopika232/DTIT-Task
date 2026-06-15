import pandas as pd
from sklearn.datasets import load_iris    #type:ignore
from sklearn.model_selection import train_test_split    #type:ignore
from sklearn.linear_model import LogisticRegression    #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from sklearn.metrics import accuracy_score    #type:ignore

# Dataset
data = load_iris()
X = pd.DataFrame(data.data)
y = data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)

# Single model
single_model = LogisticRegression(max_iter=200)
single_model.fit(X_train,y_train)
single_pred = single_model.predict(X_test)
single_accuracy = accuracy_score(y_test,single_pred)

# Ensemble model
ensemble_model = RandomForestClassifier(n_estimators=100)
ensemble_model.fit(X_train,y_train)
ensemble_pred = ensemble_model.predict(X_test)
ensemble_accuracy = accuracy_score(y_test,ensemble_pred)
print("Single Model Accuracy:",single_accuracy)
print("Ensemble Model Accuracy:",ensemble_accuracy)



####    OUTPUT    ####
# Single Model Accuracy: 1.0
# Ensemble Model Accuracy: 1.0