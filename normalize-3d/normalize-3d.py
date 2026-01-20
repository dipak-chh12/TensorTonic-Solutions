import numpy as np

def normalize_3d(v):
    v = np.array(v, dtype=np.float64)
    
   
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    
   
    return np.divide(v, norm, out=np.zeros_like(v), where=norm!=0)