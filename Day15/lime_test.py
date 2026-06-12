import pandas as pd
from sklearn.datasets import load_iris  #type:ignore
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from lime import lime_tabular #type:ignore
import warnings

warnings.filterwarnings("ignore")


# Dataset
data = load_iris()
X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,y_train)

print("Accuracy:")
print(model.score(X_test,y_test))


# LIME
explainer = lime_tabular.LimeTabularExplainer(
    X_train.values,
    feature_names=X_train.columns,
    class_names=["Setosa","Versicolor","Virginica"],mode="classification")


# Explain first prediction
exp = explainer.explain_instance(X_test.iloc[0],model.predict_proba,num_features=4)
print("\nPrediction Explanation:")
for item in exp.as_list():
    print(item)


###     OUTPUT    ###

# python lime_test.py
# Accuracy:
# 1.0

# Prediction Explanation:
# ('4.25 < petal length (cm) <= 5.10', 0.20732550489134202)
# ('0.30 < petal width (cm) <= 1.30', 0.16376470321801567)
# ('sepal width (cm) <= 2.80', -0.018957951738503894)
# ('5.75 < sepal length (cm) <= 6.40', 0.010730762302317481)