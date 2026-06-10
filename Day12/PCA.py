import pandas as pd
import matplotlib.pyplot as plt   #type:ignore
from sklearn.decomposition import PCA    #type:ignore
from sklearn.preprocessing import LabelEncoder, StandardScaler     #type:ignore


# Load dataset
data = pd.read_csv("customer.csv")


# Encode categorical columns
encoder = LabelEncoder()

data["Contract"] = encoder.fit_transform(data["Contract"])
data["Churn"] = encoder.fit_transform(data["Churn"])

# Create features
X = data.drop("Churn", axis=1)

# Scale data before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

print("Original shape:")
print(X.shape)

print("After PCA:")
print(X_reduced.shape)

# Visualization
plt.scatter(X_reduced[:,0],X_reduced[:,1])
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.title("PCA Noise Reduction")
plt.show()


####      OUTPUT     #####

# Original shape:
# (10, 5)
# After PCA:
# (10, 2)


#plot shown