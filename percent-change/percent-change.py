def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    res = []

    for i in range(1, len(series)):
        prev = series[i - 1]
        if prev == 0:
            res.append(0.0)
        else:
            res.append((series[i] - prev) / prev)

    return res
