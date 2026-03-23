import numpy as np

def f1_micro(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    correct = np.sum(y_true == y_pred)
    incorrect = np.sum(y_true != y_pred)

    if correct == 0:
        return 0.0

    return (2 * correct) / (2 * correct + 2 * incorrect)