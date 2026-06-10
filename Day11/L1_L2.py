from sklearn.datasets import load_diabetes      #type:ignore
from sklearn.linear_model import LinearRegression,Ridge,Lasso         #type:ignore
from sklearn.model_selection import train_test_split        #type:ignore
from sklearn.metrics import mean_squared_error        #type:ignore

data = load_diabetes()

X=data.data
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Linear
linear = LinearRegression()
linear.fit(X_train,y_train)
p1 = linear.predict(X_test)



# Ridge L2
ridge = Ridge(alpha=1)
ridge.fit(X_train,y_train)

p2 = ridge.predict(X_test)

# Lasso L1
lasso = Lasso(alpha=0.1)
lasso.fit(X_train,y_train)
p3 = lasso.predict(X_test)

print("Linear MSE:",mean_squared_error(y_test,p1))
print("Ridge MSE:",mean_squared_error(y_test,p2))
print("Lasso MSE:",mean_squared_error(y_test,p3))

print("\nCoefficients")

print("Linear:",linear.coef_)

print("Ridge:",ridge.coef_)

print("Lasso:",lasso.coef_)


####       OUTPUT        ####

# Linear MSE: 2900.19362849348
# Ridge MSE: 3077.41593882723
# Lasso MSE: 2798.193485169719

# Coefficients
# Linear: [  37.90402135 -241.96436231  542.42875852  347.70384391 -931.48884588
#   518.06227698  163.41998299  275.31790158  736.1988589    48.67065743]
# Ridge: [  45.36737726  -76.66608563  291.33883165  198.99581745   -0.53030959
#   -28.57704987 -144.51190505  119.26006559  230.22160832  112.14983004]
# Lasso: [   0.         -152.66477923  552.69777529  303.36515791  -81.36500664
#    -0.         -229.25577639    0.          447.91952518   29.64261704]