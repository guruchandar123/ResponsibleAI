import pandas as pd
from sklearn.metrics import confusion_matrix

def check_bias(y_true, y_pred, sensitive_features):
    results = {}
    for feature in sensitive_features.unique():
        mask = (sensitive_features == feature)
        cm = confusion_matrix(y_true[mask], y_pred[mask])
        results[feature] = cm
    return results
