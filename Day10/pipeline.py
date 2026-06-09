from sklearn.pipeline import Pipeline #type:ignore
from sklearn.preprocessing import StandardScaler    #type:ignore
from sklearn.svm import SVC     #type:ignore
from sklearn.datasets import load_iris    #type:ignore

data = load_iris()

X = data.data
y = data.target

pipeline = Pipeline([("scaler", StandardScaler()),("model", SVC())])


pipeline.fit(X,y)
result = pipeline.predict([[5.1,3.5,1.4,0.2]])

print("Class:", result[0])

print(
    "Flower:",
    data.target_names[result[0]]
)
print("Prediction:",result)

#####    OUTPUT   #####
# Class: 0
# Flower: setosa
# Prediction: [0]
