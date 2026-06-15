import numpy as np
from sklearn.linear_model import LogisticRegression        #type:ignore
from sklearn.metrics import accuracy_score        #type:ignore


# Old data
X_train = np.array([[20,50000],[25,60000],[30,80000],[35,90000]])
y_train = np.array([0,0,1,1])

# Train model
model = LogisticRegression()
model.fit(X_train,y_train)

# Test before update
X_test = np.array([[28,70000],[40,100000]])
y_test = np.array([1,1])

prediction = model.predict(X_test)
print("Before Update Accuracy:")
print(accuracy_score(y_test,prediction))

# New data
new_X = np.array([[22,55000],[45,120000]])
new_y = np.array([0,1])

# Update model
X_train = np.vstack((X_train,new_X))
y_train = np.append(y_train,new_y)

model.fit(X_train,y_train)

# Test after update
prediction = model.predict(X_test)

print("After Update Accuracy:")
print(accuracy_score(y_test,prediction))

print("Model updated successfully")



#####    OUTPUT    #####

# Before Update Accuracy:
# 0.5
# After Update Accuracy:
# 1.0
# Model updated successfully