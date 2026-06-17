import pandas as pd
import pickle
from sklearn.metrics import (accuracy_score,classification_report) #type:ignore

data = pd.read_csv("attendance/attendance.csv")

data["present"] = data["status"].apply(
lambda x:1 if x=="Present" else 0 )

X=data[["present"]]
y=data["status"]

model = pickle.load(open("models/attendance_model.pkl","rb"))
prediction=model.predict(X)
print("Accuracy:")
print(accuracy_score(y,prediction))
print(classification_report(y,prediction))