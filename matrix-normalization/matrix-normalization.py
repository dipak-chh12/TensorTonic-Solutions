import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix = np.asarray(matrix, dtype=float)

        if matrix.ndim != 2:
            return None

        if axis not in (0, 1, None):
            return None

        if norm_type == "l1":
            norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
        elif norm_type == "l2":
            norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
        elif norm_type == "max":
            norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
        else:
            return None

        norm[norm == 0] = 1

        return matrix / norm

    except:
        return None