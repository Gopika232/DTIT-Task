import pandas as pd
from sklearn.preprocessing import StandardScaler      #type:ignore

# Load dataset
data = pd.read_csv("data.csv")

print("Original Data")
print(data)

# Separate features
X = data.iloc[:, :-1]

# Preprocessing
scaler = StandardScaler()

processed_data = scaler.fit_transform(X)

print("\nPreprocessed Data")
print(processed_data)



#####   OUTPUT     ####

# Original Data
#    age  salary
# 0   20   50000
# 1   25   60000
# 2   30   80000
# 3   35   90000

# Preprocessed Data
# [[-1.34164079]
#  [-0.4472136 ]
#  [ 0.4472136 ]
#  [ 1.34164079]]