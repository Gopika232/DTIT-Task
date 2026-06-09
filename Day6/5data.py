import pandas as pd


df = pd.read_csv("data.csv")
print(df.head())


####        OUTPUT       ####

#    ID   Name  Age Department  Salary        City
# 0   1   John   25         IT   50000     Chennai
# 1   2  Alice   28         HR   45000  Coimbatore
# 2   3    Bob   22         IT   55000     Madurai
# 3   4   Emma   30    Finance   60000       Salem
# 4   5  David   27         IT   52000      Trichy