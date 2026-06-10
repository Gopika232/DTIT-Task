import pandas as pd
from sklearn.model_selection import train_test_split #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from sklearn.preprocessing import LabelEncoder   #type:ignore
from sklearn.metrics import accuracy_score   #type:ignore


# Load dataset
data = pd.read_csv("customer.csv")


# preprocessing function
def preprocess_data(data):

    encoder = LabelEncoder()

    data["Contract"] = encoder.fit_transform(data["Contract"])
    data["Churn"] = encoder.fit_transform(data["Churn"])

    return data


# preprocess
data = preprocess_data(data)

# Split data
X = data.drop("Churn", axis=1)
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# AI model
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)


# prediction

prediction = model.predict(X_test)

print("Predictions:")
print(prediction)
print("Accuracy:")
print(accuracy_score(y_test,prediction))


####    OUTPUT    ####

# Predictions:
# [1 0]
# Accuracy:
# 1.0