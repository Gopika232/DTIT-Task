import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler   #type:ignore

# Create Dataset
data = {"Age": [25, 30, np.nan, 35, 40],"Salary": [30000, 50000, 45000, np.nan, 80000],"Experience": [2, 5, 4, 8, 10]}

df = pd.DataFrame(data)
print("Original Data")
print(df)

# Handling Missing Values
df = df.fillna(df.mean())
print("\nAfter Handling Missing Values")
print(df)

# Normalizing Features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(scaled_data,columns=df.columns)

print("\nNormalized Features")
print(normalized_df)


####     OUTPUT    ####

# Original Data
#     Age   Salary  Experience
# 0  25.0  30000.0           2
# 1  30.0  50000.0           5
# 2   NaN  45000.0           4
# 3  35.0      NaN           8
# 4  40.0  80000.0          10

# After Handling Missing Values
#     Age   Salary  Experience
# 0  25.0  30000.0           2
# 1  30.0  50000.0           5
# 2  32.5  45000.0           4
# 3  35.0  51250.0           8
# 4  40.0  80000.0          10

# Normalized Features
#    Age    Salary  Experience
# 0 -1.5 -1.308467   -1.330266
# 1 -0.5 -0.076969   -0.280056
# 2  0.0 -0.384843   -0.630126
# 3  0.5  0.000000    0.770154
# 4  1.5  1.770279    1.470294