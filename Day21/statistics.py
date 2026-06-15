import pandas as pd
import numpy as np

# Create NumPy array
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])

# Convert array to DataFrame
df = pd.DataFrame(arr,columns=["A","B","C"])

print("DataFrame:")
print(df)

# Statistical analysis
print("\nMean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

print("\nSummary:")
print(df.describe())



#####    OUTPUT    #####

# DataFrame:
#     A   B   C
# 0  10  20  30
# 1  40  50  60
# 2  70  80  90

# Mean:
# A    40.0
# B    50.0
# C    60.0
# dtype: float64

# Median:
# A    40.0
# B    50.0
# C    60.0
# dtype: float64

# Standard Deviation:
# A    30.0
# B    30.0
# C    30.0
# dtype: float64

# Summary:
#           A     B     C
# count   3.0   3.0   3.0
# mean   40.0  50.0  60.0
# std    30.0  30.0  30.0
# min    10.0  20.0  30.0
# 25%    25.0  35.0  45.0
# 50%    40.0  50.0  60.0
# 75%    55.0  65.0  75.0
# max    70.0  80.0  90.0