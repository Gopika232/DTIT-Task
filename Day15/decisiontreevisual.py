import pandas as pd
import matplotlib.pyplot as plt   #type:ignore
from sklearn.datasets import load_iris #type:ignore 
from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.tree import DecisionTreeClassifier    #type:ignore
from sklearn.tree import plot_tree, export_text   #type:ignore

# Load dataset
data = load_iris()

X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# Create Decision Tree model
tree_model = DecisionTreeClassifier(max_depth=3,random_state=42)

# Train model
tree_model.fit(X_train,y_train)


# Accuracy
print("Accuracy:")
print(tree_model.score(X_test,y_test))


# Print decision rules
rules = export_text(tree_model,feature_names=list(X.columns))

print("\nDecision Tree Rules:\n")
print(rules)


# Visualize tree
plt.figure(figsize=(15,8))


plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=["Setosa","Versicolor","Virginica"],filled=True,rounded=True)

plt.title("Decision Tree Visualization")
plt.savefig("decision_tree.png")
plt.show()


####   OUTPUT    ####

#Plot shown

# Accuracy:
# 1.0

# Decision Tree Rules:

# |--- petal length (cm) <= 2.45
# |   |--- class: 0
# |--- petal length (cm) >  2.45
# |   |--- petal length (cm) <= 4.75
# |   |   |--- petal width (cm) <= 1.65
# |   |   |   |--- class: 1
# |   |   |--- petal width (cm) >  1.65
# |   |   |   |--- class: 2
# |   |--- petal length (cm) >  4.75
# |   |   |--- petal width (cm) <= 1.75
# |   |   |   |--- class: 1
# |   |   |--- petal width (cm) >  1.75
# |   |   |   |--- class: 2
