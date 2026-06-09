# normalized = (value - min)/(max-min)

import numpy as np


def normalize(arr):

    minimum = np.min(arr)
    maximum = np.max(arr)
    result = (arr - minimum) / (maximum - minimum)
    return result


data = np.array([10,20,30,40,50])

print(normalize(data))


####    OUTPUT   ####
# [0.   0.25 0.5  0.75 1.  ]
