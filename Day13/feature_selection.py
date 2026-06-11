from sklearn.datasets import load_iris  #type:ignore
from sklearn.feature_selection import SelectKBest, f_classif   #type:ignore
import numpy as np


# Load dataset
data = load_iris()

X = data.data
y = data.target


# Feature names
features = data.feature_names
features = np.array(data.feature_names)
# Select top 3 features
selector = SelectKBest(score_func=f_classif,k=3)
# Apply selection
X_selected = selector.fit_transform(X,y)


# Display selected features
print("Selected Features:")
for feature in features[selector.get_support()]:
    print(feature)

# Display scores
print("\nFeature Scores:")
for name, score in zip(features,selector.scores_):
    print(name, ":", score)


####   OUTPUT    ####

# Selected Features:
# sepal length (cm)
# petal length (cm)
# petal width (cm)

# Feature Scores:
# sepal length (cm) : 119.26450218449871
# sepal width (cm) : 49.16004008961098
# petal length (cm) : 1180.1611822529776
# petal width (cm) : 960.0071468018025