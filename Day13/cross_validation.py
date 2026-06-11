from sklearn.datasets import load_iris #type:ignore
from sklearn.model_selection import cross_val_score  #type:ignore
from sklearn.linear_model import LogisticRegression   #type:ignore


# Load dataset
data = load_iris()
X = data.data
y = data.target

# Create model
model = LogisticRegression(max_iter=500)

# Apply 5-Fold Cross Validation
scores = cross_val_score(model,X,y,cv=5)

# Display results
print("Cross Validation Scores:")
print(scores)


print("\nAverage Accuracy:")
print(scores.mean())


####    OUTPUT     ####

# Cross Validation Scores:
# [0.96666667 1.         0.93333333 0.96666667 1.        ]

# Average Accuracy:
# 0.9733333333333334