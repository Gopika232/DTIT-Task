from sklearn.metrics import precision_score,recall_score #type:ignore

# TP = True Positive
# TN = True Negative
# FP = False Positive
# FN = False Negative

#####       PRECISION     #####

#      Precision=TP/(TP+FP)

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

precision = precision_score(y_true, y_pred)
print("Precision:", precision)

###---------------OUTPUT----------###
#           Precision: 1.0

#############     RECALL         #######

#       Recall = TP/(TP+TN)

recall = recall_score(y_true, y_pred)
print("Recall:", recall)

###     OUTPUT    ###
#  Recall: 0.6666666666666666