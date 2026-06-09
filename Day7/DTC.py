from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt 


X = [[20,1],[25,1],[15,0],[10,0]]
y = ["Pass","Pass","Fail","Fail"]

model = DecisionTreeClassifier()
model.fit(X,y)


print(model.predict([[22,1]]))
plot_tree(model)
plt.show()
