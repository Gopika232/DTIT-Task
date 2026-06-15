import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data.csv")

# Create encoder
encoder = LabelEncoder()

# Encode categorical columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = encoder.fit_transform(df[col])

print("After Label Encoding:")
print(df.head())



####     OUTPUT    ####

# After Label Encoding:
#    Name   Age   Salary  Department  Experience
# 0     2  22.0  35000.0           2           1
# 1     4  25.0  45000.0           1           3
# 2     0   NaN  50000.0           2           5
# 3     3  30.0      NaN           0           7
# 4     1  28.0  60000.0           3           4