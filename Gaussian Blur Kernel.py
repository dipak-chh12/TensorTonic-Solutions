import math

def gaussian_kernel(size: int, sigma: float):
    """
    Generate a normalized 2D Gaussian kernel.
    """
    assert size % 2 == 1, "Kernel size must be odd"
    assert sigma > 0, "Sigma must be positive"

    center = size // 2
    kernel = [[0.0 for _ in range(size)] for _ in range(size)]
    total = 0.0

    for i in range(size):
        for j in range(size):
            x = j - center
            y = i - center
            value = math.exp(-(x*x + y*y) / (2 * sigma * sigma))
            kernel[i][j] = value
            total += value

    # Normalize
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= total

    return kernel
