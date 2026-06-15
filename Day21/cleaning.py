import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove rows with missing values
df = df.dropna()

print("\nCleaned Data:")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)



####   OUTPUT   ####

# Original Data:
#       Name   Age       City  Marks
# 0   Gopika  22.0    Chennai     85
# 1     Arun  21.0    Chennai     90
# 2    Priya   NaN  Bangalore     78
# 3  Karthik  23.0    Chennai     88
# 4     Arun  21.0    Chennai     90

# Missing Values:
# Name     0
# Age      1
# City     1
# Marks    0
# dtype: int64

# Cleaned Data:
#       Name   Age       City  Marks
# 0   Gopika  22.0    Chennai     85
# 1     Arun  21.0    Chennai     90
# 2    Priya  22.5  Bangalore     78
# 3  Karthik  23.0    Chennai     88
