from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.linear_model import LinearRegression     #type:ignore
from sklearn.metrics import mean_squared_error, r2_score    #type:ignore


# Dataset
X = [[1000],[1500],[2000],[2500],[3000]]
y = [200000, 300000, 400000, 500000, 600000]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Predicted Values:", y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


####  OUTPUT  ####

# Predicted Values: [300000.]
# Mean Squared Error: 3.3881317890172014e-21
# R2 Score: nan