def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds using linear interpolation.
    """
    if not values:
        return []

    if not (0 <= lower_pct <= upper_pct <= 100):
        raise ValueError("Percentiles must satisfy 0 ≤ lower_pct ≤ upper_pct ≤ 100")

    def percentile_linear(sorted_vals, p):
        n = len(sorted_vals)
        k = (n - 1) * p / 100
        i = int(k)
        j = min(i + 1, n - 1)
        if i == j:
            return sorted_vals[i]
        return sorted_vals[i] + (k - i) * (sorted_vals[j] - sorted_vals[i])

    sorted_vals = sorted(values)
    lower = percentile_linear(sorted_vals, lower_pct)
    upper = percentile_linear(sorted_vals, upper_pct)

    return [
        lower if v < lower else
        upper if v > upper else
        v
        for v in values
    ]
