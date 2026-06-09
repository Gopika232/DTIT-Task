from sklearn.model_selection import GridSearchCV #type:ignore
from sklearn.svm import SVC  #type:ignore

X = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]

y = [0,1,1,1,1,0,0,0]

model = SVC()

params = {"C":[0.1,1,10],"kernel":["linear","rbf"]}


grid = GridSearchCV(model,params,cv=3)

grid.fit(X,y)

print("Best Parameters:")
print(grid.best_params_)


####   OUTPUT    ####
# Best Parameters:
# {'C': 10, 'kernel': 'rbf'}