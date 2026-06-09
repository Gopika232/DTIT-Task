import pandas as pd
from sklearn.preprocessing import LabelEncoder  #type:ignore
from sklearn.preprocessing import StandardScaler #type:ignore


# Load cleaned dataset

df = pd.read_csv("cleaned_data.csv")

print("Original Data:")
print(df.head())

# Original Data:
#    Employee_ID     Name   Age Department        Salary  Experience        City Performance
# 0          101     Arun  25.0         IT  45000.000000           2     Chennai        Good
# 1          102    Divya  28.0         HR  52000.000000           5  Coimbatore   Excellent
# 2          103  Karthik  30.0    Finance  60000.000000           7     Madurai        Good
# 3          104    Meena  26.0         IT  55230.769231           3     Chennai     Average
# 4          105     Ravi  35.0  Marketing  75000.000000          10       Salem   Excellent


# Encode categorical variables
encoder = LabelEncoder()


for col in df.select_dtypes(include="object").columns:
    df[col] = encoder.fit_transform(df[col])

print("\nAfter Encoding:")
print(df.head())

# After Encoding:
#    Employee_ID  Name   Age  Department        Salary  Experience  City  Performance
# 0          101     2  25.0           2  45000.000000           2     0            2
# 1          102     3  28.0           1  52000.000000           5     1            1
# 2          103     4  30.0           0  60000.000000           7     2            2
# 3          104     7  26.0           2  55230.769231           3     0            0
# 4          105    10  35.0           3  75000.000000          10     3            1



# Scaling numerical values

scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=["int64","float64"]).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\nAfter Scaling:")
print(df.head())

# After Scaling:
#    Employee_ID      Name       Age  Department    Salary  Experience      City  Performance
# 0    -1.612452 -1.116313 -0.949808    0.408248 -0.986970   -1.102760 -1.185854     1.028992
# 1    -1.364382 -0.868243 -0.023745   -0.544331 -0.311675   -0.050125 -0.632456    -0.171499
# 2    -1.116313 -0.620174  0.593630   -1.496910  0.460091    0.651631 -0.079057     1.028992
# 3    -0.868243  0.124035 -0.641120    0.408248  0.000000   -0.751882 -1.185854    -1.371989
# 4    -0.620174  0.868243  2.137067    1.360828  1.907153    1.704266  0.474342    -0.171499

# Save final dataset
df.to_csv("ml_ready_data.csv",index=False)
print("\nML Dataset Ready")