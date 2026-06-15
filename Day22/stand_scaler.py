import pandas as pd
from sklearn.preprocessing import StandardScaler  #type:ignore

# Load dataset
df = pd.read_csv("data.csv")

# Select numerical columns
numeric_columns = df.select_dtypes(include=['int64','float64']).columns

# Create scaler
scaler = StandardScaler()

# Scale features
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

print("After Standard Scaling:")
print(df.head())



####    OUTPUT    ####

# After Standard Scaling:
#      Name       Age   Salary Department  Experience
# 0  Gopika -1.402136 -1.38675         IT        -1.5
# 1   Priya -0.412393 -0.27735         HR        -0.5
# 2    Arun       NaN  0.27735         IT         0.5
# 3   Kumar  1.237179      NaN    Finance         1.5
# 4   Divya  0.577350  1.38675        NaN         0.0