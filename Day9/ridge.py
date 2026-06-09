from sklearn.linear_model import Ridge #type:ignore

# Dataset
X = [[1,2],[2,3],[3,4],[4,5]]

y = [5,7,9,11]

# Ridge model
model = Ridge(alpha=1.0)

model.fit(X,y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


###   OUTPUT   ###
# Coefficients: [0.90909091 0.90909091]
# Intercept: 2.545454545454546