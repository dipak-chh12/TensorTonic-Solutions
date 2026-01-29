import numpy as np

def r2_score(y_true, y_pred) -> float:

    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    nume = np.sum((y_true-y_pred)**2)
    denom = np.sum((y_true-np.mean(y_true))**2)

    if denom == 0:
      if nume ==0:
        return 1.0
      else:
        return 0.0
    return 1 - nume/denom
