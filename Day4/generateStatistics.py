import pandas as pd

df = pd.read_csv("students.csv")

# Summary statistics and include non-numeric values

print(df.describe(include='all'))


###Output

#               ID  Name        Age     City      Marks Result
# count   20.00000    20  20.000000       20  20.000000     20
# unique       NaN    20        NaN       20        NaN      2
# top          NaN  John        NaN  Chennai        NaN   Pass
# freq         NaN     1        NaN        1        NaN     14
# mean    10.50000   NaN  23.000000      NaN  68.150000    NaN
# std      5.91608   NaN   1.450953      NaN  21.675295    NaN
# min      1.00000   NaN  21.000000      NaN  33.000000    NaN
# 25%      5.75000   NaN  22.000000      NaN  47.250000    NaN
# 50%     10.50000   NaN  23.000000      NaN  74.500000    NaN
# 75%     15.25000   NaN  24.000000      NaN  85.750000    NaN
# max     20.00000   NaN  25.000000      NaN  97.000000    NaN