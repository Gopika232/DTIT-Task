import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
data = {
    "Height":[150,120,160,170,180],
    "Weight":[50,40,60,70,80]
}

df = pd.DataFrame(data)

print("Original Dataframe: ")
print(df)

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print("\nScaled Dataframe: ")
print(scaled_df)