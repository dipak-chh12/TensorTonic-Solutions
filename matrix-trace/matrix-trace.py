import numpy as np

def matrix_trace(A):
    
    A = np.array(A)
    
   
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        
        raise ValueError("Input must be a square matrix.")
        
    return np.trace(A)
