import pandas as pd

# Load Dataset
dataset = pd.read_csv("real_world_data.csv")

# Check Missing Values
missing_values = dataset.isnull().sum()

print("Missing Values in Each Column:")
print(missing_values)

####    OUTPUT    ####

# Missing Values in Each Column:
# Name                 0
# Age                  1
# Salary               2
# Department           0
# UnnecessaryColumn    0
# dtype: int64