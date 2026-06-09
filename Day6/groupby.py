
import pandas as pd

df = pd.read_csv("data.csv")

group = df.groupby("Department")["Salary"].mean()

print(group)

####      OUTPUT      ####
# Department
# Finance      67500.0
# HR           46500.0
# IT           55500.0
# Marketing    43500.0
# Name: Salary, dtype: float64