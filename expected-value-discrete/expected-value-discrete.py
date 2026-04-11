def expected_value_discrete(x, p):
    x = np.asarray(x)
    p = np.asarray(p)
    
    if len(x) != len(p):
        raise ValueError("x and p must have same length")
    
    if not np.isclose(np.sum(p), 1):
        raise ValueError("Probabilities must sum to 1")
    
    return np.dot(x, p)