from sklearn.cluster import KMeans #type:ignore


# Dataset

X = [[1,2],[2,3],[3,4],[8,9],[9,10],[10,11]]


# Create model

kmeans = KMeans(n_clusters=2,random_state=0)


# Train
kmeans.fit(X)


# Cluster labels
print("Cluster Labels:")
print(kmeans.labels_)


# Centers

print("\nCluster Centers:")
print(kmeans.cluster_centers_)


# Interpretation

print("""
Cluster 0:
Values close to first group (1,2,3)

Cluster 1:
Values close to second group (8,9,10)

Cluster centers represent the average point of each cluster.""")



####       OUTPUT      ####


# Cluster Labels:
# [1 1 1 0 0 0]

# Cluster Centers:
# [[ 9. 10.]
#  [ 2.  3.]]

# Cluster 0:
# Values close to first group (1,2,3)

# Cluster 1:
# Values close to second group (8,9,10)

# Cluster centers represent the average point of each cluster.