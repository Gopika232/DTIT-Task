import numpy as np
from sklearn.linear_model import LinearRegression #type:ignore


X = np.array([[1],[2],[3],[4]])
y = np.array([10000,20000,30000,40000])


model = LinearRegression()
model.fit(X,y)

print("Coefficient:",model.coef_)
print("Intercept:",model.intercept_)
print("Prediction:",model.predict([[5]]))

####    OUTPUT   ####
# Coefficient: [10000.]
# Intercept: 3.637978807091713e-12
# Prediction: [50000.]