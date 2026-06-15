import pandas as pd
import numpy as np

# Create DataFrame
data = {"Name": ["A", "B", "C"],"Marks": [80, 90, 70]}

df = pd.DataFrame(data)

print("Before Transformation:")
print(df)


# Using NumPy operation
df["Normalized_Marks"] = np.round(df["Marks"] / 100,2)

print("\nAfter Transformation:")
print(df)



#####   OUTPUT    #####

# Before Transformation:
#   Name  Marks
# 0    A     80
# 1    B     90
# 2    C     70

# After Transformation:
#   Name  Marks  Normalized_Marks
# 0    A     80               0.8
# 1    B     90               0.9
# 2    C     70               0.7