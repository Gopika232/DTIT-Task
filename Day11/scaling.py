import pandas as pd

from sklearn.model_selection import train_test_split      #type:ignore
from sklearn.linear_model import LinearRegression    #type:ignore
from sklearn.preprocessing import StandardScaler          #type:ignore
from sklearn.metrics import mean_squared_error,r2_score    #type:ignore

data = pd.read_csv("house.csv")

X = data[['area','rooms']]
y = data['price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Without Scaling
model = LinearRegression()

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Before Scaling")
print("MSE:",mean_squared_error(y_test,pred))

print("R2 Score:",
r2_score(y_test,pred))

# With Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled,y_train)

pred_scaled = model.predict(X_test_scaled)

print("\nAfter Scaling")
print("MSE:",mean_squared_error(y_test,pred_scaled))
print("R2 Score:",r2_score(y_test,pred_scaled))



#####        OUTPUT        #####

# Before Scaling
# MSE: 116818343385.56027
# R2 Score: 0.9926988535384025

# After Scaling
# MSE: 116818343385.55997
# R2 Score: 0.9926988535384025

