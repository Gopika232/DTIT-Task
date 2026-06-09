from sklearn.metrics import f1_score #type:ignore



# F1 = 2*((Precision * Recall)/(Precision + Recall))

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

f1 = f1_score(y_true, y_pred)
print("F1 Score:", f1)


#####     OUTPUT      ####
#        F1 Score: 0.8