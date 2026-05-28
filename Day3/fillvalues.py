import numpy as np
import pandas as pd

data = {
    "Name":["A","B","C","D"],
    "Age":[25,30,np.nan,35],
    "Marks":[85,90,95,np.nan]
}
df = pd.DataFrame(data)
print("Original Dataframe:")
print(df)

# Filling missing values with a specific value
df["Age"].fillna(df["Age"].mean(), inplace =True)
df["Marks"].fillna(df["Marks"].mean(), inplace =True)
print("\nDataframe after filling missing values:")
print(df)
