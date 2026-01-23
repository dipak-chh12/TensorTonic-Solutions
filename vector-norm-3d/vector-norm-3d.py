import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean (L2) norm of 3D vector(s).
    """
    v = np.asarray(v)

    if v.ndim == 1:
        # single 3D vector
        return np.sqrt(np.sum(v ** 2))

    elif v.ndim == 2:
        # batch of 3D vectors
        return np.sqrt(np.sum(v ** 2, axis=1))

    else:
        raise ValueError("Input must be a 3D vector or a batch of 3D vectors")
