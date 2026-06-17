import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.linear_model import LogisticRegression    #type:ignore
from sklearn.preprocessing import LabelEncoder    #type:ignore

# load attendance data
file = "attendance/attendance.csv"
if not os.path.exists(file):
    print("Attendance data not found")
    exit()
data = pd.read_csv(file)
print(data.head())
# create features
data["present"] = data["status"].apply(lambda x: 1 if x=="Present" else 0)

X = data[["present"]]
y = data["status"]

# convert labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# train model
model = LogisticRegression()
model.fit(X_train,y_train)

# save model
with open("models/attendance_model.pkl","wb") as file:
    pickle.dump(model,file)

with open("models/label_encoder.pkl","wb") as file:
    pickle.dump(encoder,file)
    
print("Model trained successfully")