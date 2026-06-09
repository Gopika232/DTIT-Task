from sklearn.metrics import classification_report #type:ignore
from sklearn.svm import SVC #type:ignore


X = [[0,0],[1,1],[2,2],[3,3]]

y = [0,1,1,1]

model = SVC(kernel="linear")
model.fit(X,y)
y_pred = model.predict(X)
print(classification_report(y,y_pred))



####    OUTPUT     ####

#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00         1
#            1       1.00      1.00      1.00         3

#     accuracy                           1.00         4
#    macro avg       1.00      1.00      1.00         4
# weighted avg       1.00      1.00      1.00         4