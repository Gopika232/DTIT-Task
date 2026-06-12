import pandas as pd

# Load Dataset
dataset = pd.read_csv("real_world_data.csv")
print("Original Dataset:")
print(dataset.head())

# Remove Unnecessary Column
dataset_cleaned = dataset.drop(["UnnecessaryColumn"],axis=1)

# Display Cleaned Dataset
print("\nCleaned Dataset:")
print(dataset_cleaned.head())


####     OUTPUT   ####

# Original Dataset:
#      Name   Age   Salary Department  UnnecessaryColumn
# 0  Gopika  22.0  35000.0         IT                101
# 1     Anu  24.0      NaN         HR                102
# 2   Priya  23.0  40000.0    Finance                103
# 3    Kavi   NaN  30000.0         IT                104
# 4   Rahul  25.0  50000.0    Finance                105

# Cleaned Dataset:
#      Name   Age   Salary Department
# 0  Gopika  22.0  35000.0         IT
# 1     Anu  24.0      NaN         HR
# 2   Priya  23.0  40000.0    Finance
# 3    Kavi   NaN  30000.0         IT
# 4   Rahul  25.0  50000.0    Finance