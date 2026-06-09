from sklearn.metrics import accuracy_score #type:ignore
# TP = True Positive
# TN = True Negative
# FP = False Positive
# FN = False Negative

# Accuracy=TP+TN/(TP+TN+FP+FN)
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)


###--------------OUTPUT----------###
#            Accuracy: 0.8