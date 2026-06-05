import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print(df.head())

###Output
#    ID   Name  Age        City  Marks Result
# 0   1   John   22     Chennai     85   Pass
# 1   2  Alice   24  Coimbatore     92   Pass
# 2   3    Bob   21     Madurai     45   Fail
# 3   4   Emma   23       Salem     78   Pass
# 4   5   Mike   25      Trichy     55   Pass