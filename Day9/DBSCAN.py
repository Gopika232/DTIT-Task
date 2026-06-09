from sklearn.cluster import DBSCAN #type:ignore

# Dataset
X = [[1,2],[2,2],[2,3],[8,7],[8,8],[25,80]]

# DBSCAN
model = DBSCAN(eps=3,min_samples=2)

labels = model.fit_predict(X)

print("Cluster Labels:", labels)

####    OUTPUT    ####
# Cluster Labels: [ 0  0  0  1  1 -1]