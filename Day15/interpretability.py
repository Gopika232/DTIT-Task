import pandas as pd
import matplotlib.pyplot as plt   #type:ignore
from sklearn.datasets import load_iris   #type:ignore
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.ensemble import RandomForestClassifier      #type:ignore
import shap #type:ignore

# Load dataset
data = load_iris()
X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,y_train)

print("Model Accuracy:")
print(model.score(X_test,y_test))


explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test,check_additivity=False)

# Summary plot
shap.summary_plot(shap_values,X_test)

#### OUTPUT  ####

# Model Accuracy:
# 1.0

#Plot shown