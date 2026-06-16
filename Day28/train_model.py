from sklearn.neighbors import KNeighborsClassifier     #type:ignore
import numpy as np
import pickle

X_train = np.array([[0.1,0.2,0.3],[0.2,0.3,0.4],[0.8,0.7,0.6],[0.9,0.8,0.7]])
y_train = ["Gopika","Gopika","Employee2","Employee2"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
pickle.dump(model,open("attendance_model.pkl","wb"))

print("Model saved")