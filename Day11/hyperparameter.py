from sklearn.datasets import load_iris         #type:ignore
from sklearn.model_selection import GridSearchCV         #type:ignore
from sklearn.svm import SVC            #type:ignore
from sklearn.model_selection import train_test_split      #type:ignore

data = load_iris()
X = data.data
y = data.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = SVC()

parameters = {'C':[0.1,1,10],'kernel':['linear','rbf'],'gamma':['scale','auto']}

grid = GridSearchCV(model,parameters,cv=5)

grid.fit(X_train,y_train)

print("Best Parameters:",grid.best_params_)
print("Best Accuracy:",grid.best_score_)


####          OUTPUT          #####


# Best Parameters: {'C': 1, 'gamma': 'scale', 'kernel': 'linear'}
# Best Accuracy: 0.9583333333333334