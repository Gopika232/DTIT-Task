import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display missing values
print("Missing values:")
print(df.isnull().sum())


# Handle numerical missing values
for col in df.select_dtypes(include=['int64','float64']).columns:
    df[col] = df[col].fillna(df[col].mean())


# Handle categorical missing values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])


print("\nAfter handling missing values:")
print(df.isnull().sum())

print(df.head())



####    OUTPUT  ####

# Missing values:
# Name          0
# Age           1
# Salary        1
# Department    1
# Experience    0
# dtype: int64

# After handling missing values:
# Name          0
# Age           0
# Salary        0
# Department    0
# Experience    0
# dtype: int64
#      Name    Age   Salary Department  Experience
# 0  Gopika  22.00  35000.0         IT           1
# 1   Priya  25.00  45000.0         HR           3
# 2    Arun  26.25  50000.0         IT           5
# 3   Kumar  30.00  47500.0    Finance           7
# 4   Divya  28.00  60000.0         IT           4