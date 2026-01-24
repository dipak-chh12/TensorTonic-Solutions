import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)
    
    if a.ndim != 1 or b.ndim !=1:
        raise ValueError
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)

    if norma == 0 or normb == 0:
        return 0.0
    
    return float(np.dot(a,b)/(norma * normb))