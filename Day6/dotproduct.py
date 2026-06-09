import numpy as np

# (2x2) × (2x2)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])


result = np.dot(A,B)

print(result)

####     OUTPUT      ####

# [[19 22]
#  [43 50]]