from sklearn.model_selection import cross_val_score   #type:ignore
from sklearn.linear_model import LinearRegression    #type:ignore


# Dataset
X = [[1000],[1200],[1500],[1800],[2000],[2200],[2500],[2700],[3000],[3500]]
y = [200000,250000,300000,350000,400000,450000,500000,550000,600000,700000]

# Create model
model = LinearRegression()

# Cross Validation
scores = cross_val_score(model,X,y,cv=5,scoring='r2')

print("Cross Validation Scores:")
print(scores)

print("Average Score:")
print(scores.mean())

######   OUTPUT   #####
# Cross Validation Scores:
# [0.89084141 0.81654151 0.93741274 0.9302109  0.98724908]
# Average Score:
# 0.9124511300860971
