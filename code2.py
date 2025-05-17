from sklearn.metrics import (

accuracy_score, precision_score, recall_score, fl_score,

confusion_matrix, roc_auc_score, roc_curve

)

import matplotlib.pyplot as plt

#Example ground truth and predictions

y_true = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0] # Actual labels

y_pred = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0] # Predicted labels

y_scores = [0.1, 0.9, 0.3, 0.8, 0.2, 0.75, 0.1, 0.6, 0.85, 0.3] 
# Predicted probabilities
#Compute metrics

accuracy accuracy_score (y_true, y_pred)

precision precision_score (y_true, y_pred)

recall recall_score (y_true, y_pred)

f1f1_score (y_true, y_pred)

roc_auc roc_auc_score (y_true, y_scores)

#Confusion matrix

cm confusion_matrix(y_true, y_pred)

tn, fp, fn, tp cm.ravel ()

specificity tn / (tn + fp)

#Print metrics

print("Accuracy:", accuracy)

print("Precision:", precision)

print("Recall (Sensitivity):", recall)

print("Specificity:", specificity)

print("F1 Score:", fl)

print("ROC AUC Score:", roc_auc)

#Plot ROC Curve

fpr, tpr, thresholds roc_curve (y_true, y_scores)

plt.figure()

plt.plot(fpr, tpr, label='ROC Curve (AUC {:.2f))'.format(roc_auc))

plt.plot([0, 1], [0, 1], 'k--') # Diagonal line

plt.xlabel('False Positive Rate')

plt.ylabel('True Positive Rate (Recall)')

plt.title('Receiver Operating Characteristic')

plt.legend (loc='lower right')

plt.grid()