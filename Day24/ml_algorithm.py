from sklearn.linear_model import LogisticRegression     #type:ignore

# Sample dataset
X = [[22, 25000],[25, 30000],[35, 50000],[45, 70000],[50, 90000]]

y = [0, 0, 1, 1, 1]   # 0 = No Purchase, 1 = Purchase

# Create model
model = LogisticRegression()

print("Algorithm Selected: Logistic Regression")
print("Reason: Suitable for binary classification problems")