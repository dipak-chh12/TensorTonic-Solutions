import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    transpose = np.transpose(X)
    expt = np.linalg.inv(np.dot(transpose,X))
    another = np.dot(transpose, y)
    return np.dot(expt,another)