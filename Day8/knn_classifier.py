from sklearn.neighbors import KNeighborsClassifier  #type:ignore
from sklearn.model_selection import train_test_split  #type:ignore
from sklearn.metrics import accuracy_score  #type:ignore


# Dataset
X = [[1, 20],[2, 21],[3, 22],[8, 30],[9, 31],[10, 32]]

# Labels
y = [0, 0, 0, 1, 1, 1]


# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)


# Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)


# Train
knn.fit(X_train,y_train)


# Prediction
y_pred = knn.predict(X_test)


print("Predicted Values:")
print(y_pred)


# Accuracy
accuracy = accuracy_score(y_test,y_pred)

print("Accuracy:")
print(accuracy)


####     OUTPUT   ####

# Predicted Values:
# [1 1]
# Accuracy:
# 0.0