import pandas as pd

df = pd.read_csv("students.csv")

print(df.isnull().sum())

###Output

# ID      0
# Name    0
# Age     0
# City    0
# Marks     0
# Result    0
# dtype: int64