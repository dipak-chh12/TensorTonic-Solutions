import numpy as np

def dot_product(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.size == 0:
        return 0.0

    return float(np.sum(x * y))