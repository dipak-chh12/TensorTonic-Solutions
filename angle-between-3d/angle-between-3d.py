import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    numerator = np.dot(v,w)
    v_mag = np.linalg.norm(v)
    w_mag = np.linalg.norm(w)
    denom = v_mag* w_mag
    if denom ==0:
        return np.nan
    cos_theta = numerator/denom
    #cos_theta = np.clip(cos_theta, -1.0, 1.0)
    return np.arccos(cos_theta)