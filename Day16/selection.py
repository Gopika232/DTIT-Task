import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2     #type:ignore


# Create Dataset
data = {"Feature1": [1,2,3,4,5],"Feature2": [5,4,3,2,1],"Feature3": [2,3,4,5,6],"Feature4": [6,5,4,3,2],"Feature5": [1,3,5,7,9],"Feature6": [9,7,5,3,1],"Feature7": [2,4,6,8,10],"Feature8": [10,8,6,4,2],"Feature9": [3,5,7,9,11],"Feature10": [11,9,7,5,3],"Target": [0,1,0,1,1]}

df = pd.DataFrame(data)
X = df.drop("Target", axis=1)
y = df["Target"]

# Select Top 10 Features
selector = SelectKBest(score_func=chi2,k=10)

X_new = selector.fit_transform(X,y)

selected_features = X.columns[selector.get_support()]

print("Selected Top 10 Features:")
for feature in selected_features:
    print(feature)
print("\nFeature Data")
print(X_new)

####     OUTPUT     ####


# Selected Top 10 Features:
# Feature1
# Feature2
# Feature3
# Feature4
# Feature5
# Feature6
# Feature7
# Feature8
# Feature9
# Feature10

# Feature Data
# [[ 1  5  2  6  1  9  2 10  3 11]
#  [ 2  4  3  5  3  7  4  8  5  9]
#  [ 3  3  4  4  5  5  6  6  7  7]
#  [ 4  2  5  3  7  3  8  4  9  5]
#  [ 5  1  6  2  9  1 10  2 11  3]]