import numpy as np
from sklearn.metrics import mean_squared_error
def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    
    
    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted lists must have the same length")
    
    n = len(y_true)
    squared_errors_sum = 0
    
  
    for i in range(n):
        squared_errors_sum += (y_true[i] - y_pred[i])**2
    
   
    mse = squared_errors_sum / n
    return mse
