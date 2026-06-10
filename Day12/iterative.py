import pandas as pd
from sklearn.model_selection import train_test_split    #type:ignore
from sklearn.preprocessing import LabelEncoder          #type:ignore
from sklearn.ensemble import RandomForestClassifier     #type:ignore
from sklearn.metrics import accuracy_score              #type:ignore


# Load dataset
data = pd.read_csv("customer.csv")


# Convert categorical values
encoder = LabelEncoder()

data["Contract"] = encoder.fit_transform(data["Contract"])
data["Churn"] = encoder.fit_transform(data["Churn"])


# Split input and output

X = data.drop("Churn", axis=1)
y = data["Churn"]


# Create train and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Initial model
model1 = RandomForestClassifier(n_estimators=50,random_state=42)


model1.fit(X_train,y_train)

prediction1 = model1.predict(X_test)

print("Before Improvement:")
print(accuracy_score(y_test,prediction1))



# Improved model
model2 = RandomForestClassifier(n_estimators=200,max_depth=10,random_state=42)

model2.fit(X_train,y_train)
prediction2 = model2.predict(X_test)

print("After Improvement:")
print(accuracy_score(y_test,prediction2))


####      OUTPUT      ####

# Before Improvement:
# 1.0
# After Improvement:
# 1.0