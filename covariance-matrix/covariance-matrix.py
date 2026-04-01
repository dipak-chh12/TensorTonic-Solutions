import numpy as np

def covariance_matrix(X):
    X = np.asarray(X)
    
    #2d checkk
    if X.ndim != 2:
        return None
    
    n = X.shape[0]
    
    if n < 2:
        return None
    
    means = np.mean(X, axis=0)
    X_centered = X - means
    
    cov = (X_centered.T @ X_centered) / (n - 1)
    
    return cov