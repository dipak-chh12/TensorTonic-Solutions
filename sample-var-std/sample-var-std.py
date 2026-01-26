import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    n = x.size
    mean_x = np.mean(x)
    var = np.sum((x-mean_x)**2)/(n-1)
    return var,np.sqrt(var)