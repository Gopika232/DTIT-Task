import numpy as np
from sklearn.preprocessing import StandardScaler #type:ignore

data = np.array([[10, 100],[20, 200],[30, 300], [40, 400]])

print("Original Data:")
print(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("\nScaled Data:")
print(scaled_data)

####     OUTPUT   ####
# Original Data:

# [[ 10 100]
#  [ 20 200]
#  [ 30 300]
#  [ 40 400]]

# Scaled Data:

# [[-1.34164079 -1.34164079]
#  [-0.4472136  -0.4472136 ]
#  [ 0.4472136   0.4472136 ]
#  [ 1.34164079  1.34164079]]