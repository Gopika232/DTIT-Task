import pandas as pd
from imblearn.over_sampling import SMOTE    #type:ignore
from sklearn.preprocessing import LabelEncoder     #type:ignore
from sklearn.model_selection import train_test_split       #type:ignore
from sklearn.ensemble import RandomForestClassifier   #type:ignore
from sklearn.metrics import accuracy_score      #type:ignore

# Load dataset
data = pd.read_csv("customer.csv")

# Encode text values
encoder = LabelEncoder()
data["Contract"] = encoder.fit_transform(data["Contract"])
data["Churn"] = encoder.fit_transform(data["Churn"])

# Create X and y
X = data.drop("Churn", axis=1)
y = data["Churn"]

print("Before SMOTE:")
print(y.value_counts())

# Apply SMOTE
smote = SMOTE(random_state=42,k_neighbors=2)
X_resampled, y_resampled = smote.fit_resample(X,y)

print("\nAfter SMOTE:")
print(y_resampled.value_counts())



# Split data

X_train, X_test, y_train, y_test = train_test_split(X_resampled,y_resampled,test_size=0.2,random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test,prediction))



#####     OUTPUT     #####

# Before SMOTE:
# Churn
# 0    6
# 1    4
# Name: count, dtype: int64

# After SMOTE:
# Churn
# 0    6
# 1    6
# Name: count, dtype: int64

# Accuracy:
# 0.6666666666666666