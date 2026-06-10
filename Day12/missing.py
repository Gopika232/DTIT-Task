import pandas as pd
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.impute import SimpleImputer    #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from sklearn.preprocessing import LabelEncoder    #type:ignore
from sklearn.metrics import accuracy_score    #type:ignore

# Load dataset
data = pd.read_csv("customer.csv")

# Add a missing value example
data.loc[2, "MonthlyCharges"] = None
data.loc[5, "Tenure"] = None

# Encode categorical data
encoder = LabelEncoder()
data["Contract"] = encoder.fit_transform(data["Contract"])
data["Churn"] = encoder.fit_transform(data["Churn"])

# Create X and y
X = data.drop("Churn", axis=1)
y = data["Churn"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Before handling missing values
print("Missing values before:")
print(X_train.isnull().sum())

# Fill missing values
imputer = SimpleImputer(strategy="median")

X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Model
model = RandomForestClassifier(random_state=42)

model.fit(X_train,y_train)
prediction = model.predict(X_test)

print("\nAccuracy after handling missing values:")

print(accuracy_score(y_test,prediction))


######          OUTPUT         ######

# Missing values before:
# Age               0
# MonthlyCharges    1
# Tenure            1
# SupportCalls      0
# Contract          0
# dtype: int64

# Accuracy after handling missing values:
# 1.0