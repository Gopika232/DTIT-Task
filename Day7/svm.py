from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


X = [[1,2],[2,3],[8,9],[9,10]]
y = [0,0,1,1]


model = SVC()
model.fit(X,y)
prediction = model.predict(X)
accuracy = accuracy_score(y,prediction)

print("Prediction:", prediction)
print("Accuracy:", accuracy)



####    OUTPUT   ####

# Prediction: [0 0 1 1]
# Accuracy: 1.0