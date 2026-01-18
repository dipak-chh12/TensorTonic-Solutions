import numpy as np
from collections import Counter

def mean_median_mode(x):
    mean = np.mean(x)
    median = np.median(x)

    counts = Counter(x)
    mode = counts.most_common(1)[0][0]

    return mean, median, mode
