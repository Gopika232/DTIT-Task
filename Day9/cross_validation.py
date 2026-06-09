from sklearn.model_selection import cross_val_score #type:ignore
from sklearn.svm import SVC   #type:ignore

X = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
y = [0,0,0,0,1,1,1,1]

model = SVC(kernel="linear")
scores = cross_val_score(model,X,y,cv=3)

print("Scores:", scores)
print("Average Accuracy:", scores.mean())
 ####     OUTPUT    ####
# Scores: [1.  1.  0.5]
# Average Accuracy: 0.8333333333333334